# -*- coding: utf-8 -*-
# LA GENERACIÓN DEL PDF SE HIZO CON AYUDA DE UNA INTELIGENCIA ARTIFICIAL.

"""Genera libro_de_codigos.pdf a partir del contenido estructurado."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak)

OUT = "libro_de_codigos.pdf"
NAVY = colors.HexColor("#1f3864")
LIGHT = colors.HexColor("#e8edf5")

styles = getSampleStyleSheet()
h1 = ParagraphStyle("h1", parent=styles["Title"], textColor=NAVY, fontSize=20, spaceAfter=6)
h2 = ParagraphStyle("h2", parent=styles["Heading2"], textColor=NAVY, fontSize=13, spaceBefore=14, spaceAfter=4)
h3 = ParagraphStyle("h3", parent=styles["Heading3"], textColor=colors.HexColor("#2f5496"), fontSize=11, spaceBefore=8, spaceAfter=2)
body = ParagraphStyle("body", parent=styles["Normal"], fontSize=9.5, leading=13)
small = ParagraphStyle("small", parent=styles["Normal"], fontSize=8.5, leading=11)

story = []

def P(t, s=body): story.append(Paragraph(t, s))
def SP(h=6): story.append(Spacer(1, h))

def kv_table(rows, widths):
    t = Table(rows, colWidths=widths)
    t.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#b9c4d9")),
        ("BACKGROUND", (0,0), (0,-1), LIGHT),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("FONTSIZE", (0,0), (-1,-1), 8.5),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ]))
    return t

def header_table(rows, widths):
    t = Table(rows, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#b9c4d9")),
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f4f7fb")]),
    ]))
    return t

# ---------------- Portada / metadatos ----------------
P("Libro de Códigos", h1)
P("Establecimientos educativos de nivel diversificado — 22 departamentos de Guatemala", h3)
P("Proyecto 1 · CC3084 Data Science · Universidad del Valle de Guatemala · Semestre II 2026", small)
SP(10)

meta = [
    ["Campo", "Valor"],
    ["Descripción", "Establecimientos educativos de Guatemala que llegan hasta el nivel diversificado "
                    "(NIVEL ESCOLAR: DIVERSIFICADO), de los 22 departamentos del país."],
    ["Fuente de los datos", "MINEDUC — http://www.mineduc.gob.gt/BUSCAESTABLECIMIENTO_GE/"],
    ["Fecha de extracción", "Julio 2026"],
    ["Fecha de limpieza", "Julio 2026"],
    ["Versión del conjunto limpio", "v1.0"],
    ["Archivo limpio", "Data/limpio/establecimientos_diversificado_limpio.csv"],
    ["Codificación", "UTF-8 con BOM"],
    ["Registros", "9,706"],
    ["Variables", "22"],
    ["Cobertura", "22 departamentos de Guatemala (país completo)"],
    ["Llave primaria", "CODIGO (única, sin repetidos)"],
]
meta = [[Paragraph(c[0], small), Paragraph(c[1], small)] for c in meta]
story.append(header_table(meta, [4.5*cm, 12*cm]))
SP(8)
P("<b>Origen de los datos crudos.</b> Los datos vinieron en 22 archivos CSV (uno por departamento), "
  "en dos estructuras: Grupo A (11 archivos, 18 columnas, con SUPERVISOR y DIRECTOR separados y una "
  "columna vacía) y Grupo B (11 archivos, 16 columnas, con SUPERVISOR_DIRECTOR fusionado y un "
  "desplazamiento de columnas hacia DEPARTAMENTAL). La limpieza los unificó en un solo conjunto. "
  "El proceso reproducible está en code/limpieza.ipynb (usa code/limpieza_lib.py).", body)

story.append(PageBreak())

# ---------------- Diccionario de variables ----------------
P("Diccionario de variables", h2)
P("Para cada variable: descripción, tipo, dominio permitido, valores posibles, tratamiento aplicado "
  "y porcentaje de faltantes en el conjunto limpio.", small)
SP(4)

VARS = [
    ("1. CODIGO", "texto (identificador)", "Patrón NN-NN-NNNN-NN",
     "9,706 valores únicos (uno por registro).",
     "Ninguno; se verificó formato (100% conforme) y unicidad. Es la llave primaria.", "0%"),
    ("2. DISTRITO", "texto (código)", "NN-NN-NNNN o NN-NNN", "1,590 códigos.",
     "Se conservaron los dos formatos válidos; los truncados imposibles (17-, 10-) se pasaron a NA (3 registros).", "3.27%"),
    ("3. DEPARTAMENTO", "categórico", "Los 22 departamentos oficiales de Guatemala.",
     "ALTA VERAPAZ, BAJA VERAPAZ, CHIMALTENANGO, CHIQUIMULA, EL PROGRESO, ESCUINTLA, GUATEMALA, "
     "HUEHUETENANGO, IZABAL, JALAPA, JUTIAPA, PETEN, QUETZALTENANGO, QUICHE, RETALHULEU, SACATEPEQUEZ, "
     "SAN MARCOS, SANTA ROSA, SOLOLA, SUCHITEPEQUEZ, TOTONICAPAN, ZACAPA.",
     "Mayúsculas y sin tildes (criterio unificado).", "0%"),
    ("4. MUNICIPIO", "categórico", "Municipios del departamento correspondiente.", "505 municipios.",
     "Normalización de texto (mayúsculas, espacios, invisibles).", "0%"),
    ("5. ESTABLECIMIENTO", "texto libre", "Texto.", "5,552 nombres únicos.",
     "Mayúsculas, eliminación de espacios dobles e invisibles, corrección de acento grave invertido (Ò→Ó). "
     "No se alteraron los nombres oficiales.", "1.13%"),
    ("6. DIRECCION", "texto libre", "Texto.", "5,490 direcciones únicas.",
     "Normalización de texto. En el Grupo B algunos registros traían datos mezclados; solo se corrigió con "
     "evidencia suficiente y se conservaron nulos cuando no fue posible recuperar el dato.", "6.62%"),
    ("7. TELEFONO", "texto (respaldo)", "Texto con dígitos y separadores.", "—",
     "Normalización de texto. Se conserva como respaldo; los valores usables se derivan en TELEFONO_1/TELEFONO_2.", "7.10%"),
    ("8. TELEFONO_1 (derivada)", "texto (8 dígitos)", "Exactamente 8 dígitos (estándar de Guatemala).", "—",
     "Se separó TELEFONO por sus separadores (guion, espacio, coma) y se tomó el primer número de 8 dígitos.", "7.68%"),
    ("9. TELEFONO_2 (derivada)", "texto (8 dígitos)", "Exactamente 8 dígitos.", "—",
     "Igual que TELEFONO_1, tomando el segundo número válido.", "99.11% (solo con 2 teléfonos)"),
    ("10. N_TELEFONOS (derivada)", "entero", "0, 1, 2, 3.", "—",
     "Cantidad de números válidos (8 dígitos). Permite validar formato y detectar registros sin teléfono válido.", "0%"),
    ("11. SUPERVISOR_DIRECTOR", "texto libre", "Texto (nombres de persona).", "6,136 valores únicos.",
     "En el Grupo A se fusionaron SUPERVISOR y DIRECTOR (separados por espacio) para uniformar con el Grupo B. "
     "El marcador '----' se pasó a NA. No se separaron los dos nombres en B por falta de delimitador confiable.", "5.75%"),
    ("12. NIVEL", "categórico (constante)", "DIVERSIFICADO", "DIVERSIFICADO (único valor).",
     "Se conserva como constante documentada; confirma el filtro de extracción.", "0%"),
    ("13. SECTOR", "categórico", "OFICIAL, PRIVADO, COOPERATIVA, MUNICIPAL.", "4 valores.",
     "Mayúsculas, sin tildes.", "0%"),
    ("14. AREA", "categórico", "URBANA, RURAL.", "2 valores.", "Mayúsculas, sin tildes.", "0.02%"),
    ("15. STATUS", "categórico", "ABIERTA, CERRADA TEMPORALMENTE, CERRADA DEFINITIVAMENTE, "
     "TEMPORAL NOMBRAMIENTO, TEMPORAL TITULOS.", "5 valores.",
     "En el Grupo B se recuperó desde DEPARTAMENTAL por el desplazamiento de columnas; mayúsculas, sin tildes.", "0%"),
    ("16. MODALIDAD", "categórico", "MONOLINGUE, BILINGUE.", "2 valores.",
     "Recuperación desde DEPARTAMENTAL (Grupo B); mayúsculas, sin tildes.", "0%"),
    ("17. JORNADA", "categórico", "MATUTINA, VESPERTINA, DOBLE, NOCTURNA, INTERMEDIA, SIN JORNADA.", "6 valores.",
     "Recuperación desde DEPARTAMENTAL (Grupo B); mayúsculas, sin tildes.", "0%"),
    ("18. PLAN", "categórico", "DIARIO(REGULAR), FIN DE SEMANA, SABATINO, DOMINICAL, MIXTO, IRREGULAR, "
     "A DISTANCIA, VIRTUAL A DISTANCIA, SEMIPRESENCIAL, SEMIPRESENCIAL (FIN DE SEMANA), "
     "SEMIPRESENCIAL (UN DIA A LA SEMANA), SEMIPRESENCIAL (DOS DIAS A LA SEMANA).", "12 valores.",
     "Recuperación desde DEPARTAMENTAL (Grupo B); mayúsculas, sin tildes.", "0.02%"),
    ("19. DEPARTAMENTAL", "categórico", "Los 22 departamentos, con subdivisiones legítimas: GUATEMALA "
     "(NORTE, SUR, ORIENTE, OCCIDENTE) y QUICHE (QUICHE, QUICHE NORTE). 26 jurisdicciones.", "26 valores.",
     "En el Grupo B se extrajo la jurisdicción del texto contaminado por el desplazamiento; mayúsculas, sin tildes.", "0%"),
    ("20. GRUPO_ORIGEN (derivada)", "categórico", "A, B.", "2 valores.",
     "Grupo estructural del archivo crudo de origen. Trazabilidad de origen y decisiones de limpieza.", "0%"),
    ("21. ES_POSIBLE_DUPLICADO (derivada)", "booleano", "True, False.", "2 valores.",
     "Dos registros del mismo depto y municipio con nombre casi idéntico (RapidFuzz ≥ 90), misma dirección "
     "(≥ 90) o teléfono, y coincidencia en JORNADA, PLAN, SECTOR, AREA. Marca 1,724 filas (1,030 pares). "
     "No se eliminaron: CODIGO es llave única. Detalle en Data/limpio/posibles_duplicados.csv.", "0%"),
    ("22. REVISAR_MANUAL (derivada)", "texto", "Texto o NA.", "—",
     "Marca los 4 registros del Grupo B cuyo desplazamiento dejó texto sin asignar tras el parseo. Se "
     "conservan con la jurisdicción ya extraída y una nota para revisión.", "99.96% (solo 4 registros)"),
]

for nombre, tipo, dominio, valores, trat, na in VARS:
    P(nombre, h3)
    rows = [
        [Paragraph("<b>Tipo de dato</b>", small), Paragraph(tipo, small)],
        [Paragraph("<b>Dominio permitido</b>", small), Paragraph(dominio, small)],
        [Paragraph("<b>Valores posibles</b>", small), Paragraph(valores, small)],
        [Paragraph("<b>Tratamiento aplicado</b>", small), Paragraph(trat, small)],
        [Paragraph("<b>Faltantes</b>", small), Paragraph(na, small)],
    ]
    story.append(kv_table(rows, [3.5*cm, 13*cm]))
    SP(4)

story.append(PageBreak())

# ---------------- Variables derivadas ----------------
P("Variables derivadas (resumen)", h2)
der = [["Variable", "Se creó porque", "Cómo se calculó", "Utilidad"],
    ["TELEFONO_1, TELEFONO_2", "El campo original mezclaba varios teléfonos",
     "Separando TELEFONO por sus separadores y validando 8 dígitos", "Un teléfono por columna, validable"],
    ["N_TELEFONOS", "Se necesita saber cuántos teléfonos válidos hay",
     "Conteo de números de 8 dígitos por registro", "Validación y control de calidad"],
    ["GRUPO_ORIGEN", "Los datos vinieron en dos estructuras", "Etiqueta A/B según el archivo de origen", "Trazabilidad"],
    ["ES_POSIBLE_DUPLICADO", "La guía exige detectar duplicados parciales",
     "Similitud de cadenas (RapidFuzz) + coincidencia de campos clave", "Revisión de duplicados sin borrado automático"],
    ["REVISAR_MANUAL", "Algunos casos no se resuelven sin criterio humano",
     "Marca puesta durante la reparación del desplazamiento", "Auditoría y revisión manual"]]
der = [[Paragraph(c, small) for c in row] for row in der]
story.append(header_table(der, [3.5*cm, 4*cm, 5*cm, 4*cm]))
SP(10)

P("Reproducibilidad", h2)
P("Todo el proceso es reproducible desde la raíz del repositorio:", body)
code_style = ParagraphStyle("code", parent=small, fontName="Courier", backColor=LIGHT, borderPadding=6)
P("pip install pandas numpy rapidfuzz unidecode nbformat nbconvert ipykernel<br/>"
  "python -m nbconvert --to notebook --execute --inplace code/limpieza.ipynb", code_style)
SP(4)
P("Genera Data/limpio/establecimientos_diversificado_limpio.csv y los reportes de apoyo "
  "(registro_transformaciones.csv, informe_calidad.csv, posibles_duplicados.csv).", body)

doc = SimpleDocTemplate(OUT, pagesize=letter, topMargin=1.6*cm, bottomMargin=1.6*cm,
                        leftMargin=2*cm, rightMargin=2*cm,
                        title="Libro de Códigos - Establecimientos Diversificado",
                        author="Proyecto 1 CC3084 Data Science UVG")
doc.build(story)
print("PDF generado:", OUT)

# para generar el pdf se debe entrar al archivo "Proyecto1-DataScience"
# Y luego ejecutar: "python code/generar_libro_pdf.py"
# Tiene que salir un texto de "PDF generado: libro_de_codigos.pdf"