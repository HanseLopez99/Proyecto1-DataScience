# -*- coding: utf-8 -*-
"""
limpieza_lib.py
Funciones reproducibles de limpieza para el Proyecto 1 (CC3084 - Data Science).
Establecimientos educativos hasta nivel diversificado, 22 departamentos de Guatemala.

Fuente: http://www.mineduc.gob.gt/BUSCAESTABLECIMIENTO_GE/
Todo el codigo usa rutas relativas a la raiz del repositorio.

Este modulo es importado por el notebook code/limpieza.ipynb
Se mantiene como .py aparte para que la logica sea versionable, testeable y reutilizable
"""
import os
import re
import glob
import unicodedata
import pandas as pd

# __ Rutas ________________________________________________________________
DATA_DIR = "Data"


# __ Catálogos y dominios válidos _________________________________________
# 22 departamentos oficiales de Guatemala, sin tildes (criterio unificado).
DEPARTAMENTOS = [
    "ALTA VERAPAZ", "BAJA VERAPAZ", "CHIMALTENANGO", "CHIQUIMULA", "EL PROGRESO",
    "ESCUINTLA", "GUATEMALA", "HUEHUETENANGO", "IZABAL", "JALAPA", "JUTIAPA",
    "PETEN", "QUETZALTENANGO", "QUICHE", "RETALHULEU", "SACATEPEQUEZ",
    "SAN MARCOS", "SANTA ROSA", "SOLOLA", "SUCHITEPEQUEZ", "TOTONICAPAN", "ZACAPA",
]

# Jurisdicciones departamentales (DEPARTAMENTAL) validas en el grupo B.
# Sin tildes, para unificar criterio con el grupo A.
JURISDICCIONES_B = [
    "GUATEMALA SUR", "GUATEMALA OCCIDENTE", "GUATEMALA ORIENTE", "GUATEMALA NORTE",
    "ESCUINTLA", "HUEHUETENANGO", "ALTA VERAPAZ", "CHIMALTENANGO", "IZABAL",
    "JUTIAPA", "CHIQUIMULA", "JALAPA", "BAJA VERAPAZ", "EL PROGRESO",
]

# Dominios de las 4 columnas que se desplazaron hacia DEPARTAMENTAL en el grupo B.
STATUS_DOM = [
    "CERRADA TEMPORALMENTE", "CERRADA DEFINITIVAMENTE", "TEMPORAL NOMBRAMIENTO",
    "TEMPORAL TITULOS", "SIN ESPECIFICAR", "ABIERTA",
]
MODALIDAD_DOM = ["MONOLINGUE", "BILINGUE"]
JORNADA_DOM = [
    "SIN JORNADA", "DOBLE", "VESPERTINA", "MATUTINA", "NOCTURNA",
    "INTERMEDIA", "INTERCALADO",
]
# El orden importa: primero los mas largos para que ".endswith" no corte de mas
PLAN_DOM = [
    "SEMIPRESENCIAL (UN DIA A LA SEMANA)", "SEMIPRESENCIAL (FIN DE SEMANA)",
    "SEMIPRESENCIAL (DOS DIAS A LA SEMANA)", "VIRTUAL A DISTANCIA", "A DISTANCIA",
    "SEMIPRESENCIAL", "DIARIO(REGULAR)", "FIN DE SEMANA", "SABATINO",
    "DOMINICAL", "MIXTO", "IRREGULAR",
]

# Esquema final unificado (orden de columnas del conjunto limpio)
ESQUEMA_FINAL = [
    "CODIGO", "DISTRITO", "DEPARTAMENTO", "MUNICIPIO", "ESTABLECIMIENTO",
    "DIRECCION", "TELEFONO", "TELEFONO_1", "TELEFONO_2", "N_TELEFONOS",
    "SUPERVISOR_DIRECTOR", "NIVEL", "SECTOR", "AREA", "STATUS", "MODALIDAD",
    "JORNADA", "PLAN", "DEPARTAMENTAL", "GRUPO_ORIGEN", "REVISAR_MANUAL",
]



# __ Utilidades de texto _______________________________________________
def quitar_tildes(texto):
    """Quita tildes y diacriticos, conservando la enie como N."""
    if pd.isna(texto):
        return texto
    texto = texto.replace("Ñ", "N").replace("ñ", "n")
    nfkd = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def normalizar_texto(s):
    """
    Normaliza una celda de texto libre:
    - quita caracteres invisibles (BOM, zero-width),
    - recorta espacios al inicio y final,
    - colapsa espacios multiples a uno.
    Devuelve pd.NA si queda vacio.
    """
    if pd.isna(s):
        return pd.NA
    s = str(s)
    # caracteres invisibles / de control comunes
    s = s.replace("﻿", "").replace("​", "").replace("\xa0", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s if s != "" else pd.NA


def a_nulo_marcadores(s):
    """Convierte marcadores de dato ausente ('----', 'N/A', 'NULL', '-', '.', 'SIN DATO') en NA."""
    if pd.isna(s):
        return pd.NA
    t = str(s).strip()
    marcadores = {"", "-", "--", "---", "----", ".", "..", "...",
                  "N/A", "NA", "NULL", "SIN DATO", "S/D", "#N/A"}
    if t.upper() in {m.upper() for m in marcadores} or set(t) == {"-"}:
        return pd.NA
    return s



# __ Carga ________________________________________________________
def cargar_grupo_A(data_dir=DATA_DIR):
    files = sorted(f for f in glob.glob(os.path.join(data_dir, "*diversificado.csv"))
                   if "_limpio" not in os.path.basename(f))
    frames = []
    for f in files:
        df = pd.read_csv(f, dtype=str, keep_default_na=False, na_values=[""],
                         encoding="utf-8-sig")
        df["__ARCHIVO__"] = os.path.basename(f)
        frames.append(df)
    return pd.concat(frames, ignore_index=True), files


def cargar_grupo_B(data_dir=DATA_DIR):
    files = sorted(glob.glob(os.path.join(data_dir, "*_limpio.csv")))
    frames = []
    for f in files:
        df = pd.read_csv(f, dtype=str, keep_default_na=False, na_values=[""],
                         encoding="utf-8-sig")
        df["__ARCHIVO__"] = os.path.basename(f)
        frames.append(df)
    return pd.concat(frames, ignore_index=True), files


# __ Reparacion del desplazamiento de columnas del grupo B ___________________
def _quitar_sufijo(cadena, dominio):
    for d in sorted(dominio, key=len, reverse=True):
        if cadena == d:
            return d, ""
        if cadena.endswith(" " + d):
            return d, cadena[: -(len(d) + 1)].rstrip()
    return None, cadena


def reparar_departamental_B(B):
    """
    Repara el desplazamiento de columnas del grupo B.
    Solo se rellena una columna si estaba vacia (no se sobreescribe informacion).
    """
    B = B.copy()
    # DEPARTAMENTAL sin tildes para comparar contra catalogos sin tildes.
    B["DEPARTAMENTAL"] = B["DEPARTAMENTAL"].map(
        lambda x: quitar_tildes(x) if pd.notna(x) else x)
    B["REVISAR_MANUAL"] = pd.NA

    juris_set = set(JURISDICCIONES_B)
    for idx, r in B.iterrows():
        dep = r["DEPARTAMENTAL"]
        if pd.isna(dep) or dep in juris_set:
            continue  # fila limpia, nada que reparar

        resto = dep
        juris, resto = _quitar_sufijo(resto, JURISDICCIONES_B)
        if juris is None:
            B.at[idx, "REVISAR_MANUAL"] = "DEPARTAMENTAL sin jurisdiccion reconocible"
            continue

        rellenos = {}
        # Orden de extraccion: PLAN, JORNADA, MODALIDAD, STATUS (derecha->izquierda).
        for col, dom in [("PLAN", PLAN_DOM), ("JORNADA", JORNADA_DOM),
                         ("MODALIDAD", MODALIDAD_DOM), ("STATUS", STATUS_DOM)]:
            if pd.isna(r[col]):
                val, resto = _quitar_sufijo(resto, dom)
                if val is not None:
                    rellenos[col] = val
                # si no matchea, se deja la columna en NA (no se inventa)

        # La jurisdiccion siempre se asigna (DEPARTAMENTAL queda con dominio limpio).
        B.at[idx, "DEPARTAMENTAL"] = juris
        for col, val in rellenos.items():
            B.at[idx, col] = val

        # Si sobro texto sin asignar, la fila requiere revision manual (no se adivina).
        if resto.strip() != "":
            B.at[idx, "REVISAR_MANUAL"] = f"texto no asignado tras reparar: '{resto.strip()}'"

    return B


# __ Telefonos _______________________________________________________________

def separar_telefonos(valor):

    if pd.isna(valor):
        return pd.NA, pd.NA, 0
    partes = re.split(r"[,/;\-\s]+", str(valor).strip())
    validos = [p for p in (re.sub(r"\D", "", x) for x in partes) if len(p) == 8]
    t1 = validos[0] if len(validos) >= 1 else pd.NA
    t2 = validos[1] if len(validos) >= 2 else pd.NA
    return t1, t2, len(validos)


# __ Codigos (DISTRITO) ______________________________________________________
def estandarizar_distrito(valor):
    """
    Normaliza DISTRITO al formato largo NN-NN-NNNN cuando es posible.
    - NN-NN-NNNN se deja igual.
    - NN-NNN es un formato corto valido que se conserva (no hay forma de
      inferir el bloque intermedio sin catalogo oficial); se deja tal cual.
    - Codigos truncados como '17-' o '10-' se convierten en NA (invalidos).

    Y Devuelve (valor_limpio, es_valido_bool).
    """
    if pd.isna(valor):
        return pd.NA, True
    v = str(valor).strip()
    if re.fullmatch(r"\d{2}-\d{2}-\d{4}", v):
        return v, True
    if re.fullmatch(r"\d{2}-\d{3}", v):
        return v, True
    # truncado u otro formato imposible
    return pd.NA, False
