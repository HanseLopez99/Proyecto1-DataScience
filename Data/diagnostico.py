import pandas as pd
import glob, os, re

pd.set_option("display.width", 140)

# Rutas relativas a la raiz del repositorio (este archivo esta en code/).
# Ancladas a la ubicacion del script para que corra desde cualquier carpeta.
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "Data")

files = sorted(glob.glob(os.path.join(DATA, "*_limpio.csv")))
dfs = []
resumen_base = []
for f in files:
    base = os.path.basename(f).replace('_diversificado_limpio.csv', '')
    df = pd.read_csv(f, dtype=str, keep_default_na=False, na_values=[''])
    df['__BASE__'] = base
    dfs.append(df)

full = pd.concat(dfs, ignore_index=True)
cols = [c for c in full.columns if c != '__BASE__']

print("="*70)
print("0/1. REGISTROS, VARIABLES Y BASES")
print("="*70)
print("Registros totales:", len(full))
print("Variables:", len(cols))
print("Bases:", full['__BASE__'].nunique())
print(full.groupby('__BASE__').size().to_string())

print()
print("="*70)
print("2. TIPOS DE DATO")
print("="*70)
print(full[cols].dtypes.to_string())

print()
print("="*70)
print("3. FALTANTES POR VARIABLE")
print("="*70)
faltantes = full[cols].isna().sum()
pct = (faltantes / len(full) * 100).round(2)
tabla_falt = pd.DataFrame({'no_nulos': len(full)-faltantes, 'faltantes': faltantes, 'pct_faltantes': pct})
print(tabla_falt.to_string())

print()
print("Faltantes de SUPERVISOR_DIRECTOR y TELEFONO por departamento:")
for col in ['SUPERVISOR_DIRECTOR', 'TELEFONO', 'DISTRITO']:
    print(f"-- {col} --")
    print(full[full[col].isna()].groupby('__BASE__').size().to_string())

print()
print("="*70)
print("4. VALORES UNICOS")
print("="*70)
uniq = full[cols].nunique(dropna=True)
print(uniq.to_string())

print()
print("Municipios unicos por departamento:")
print(full.groupby('__BASE__')['MUNICIPIO'].nunique().to_string())

print()
print("="*70)
print("5. DUPLICADOS EXACTOS")
print("="*70)
dups = full[cols].duplicated().sum()
print("Duplicados exactos (todas las columnas):", dups)
print("CODIGO repetidos:", full['CODIGO'].duplicated().sum())

print()
print("="*70)
print("6. DOMINIOS DE VARIABLES CATEGORICAS")
print("="*70)
for col in ['NIVEL','SECTOR','AREA','STATUS','MODALIDAD','JORNADA','PLAN']:
    print(f"-- {col} ({full[col].nunique()} valores) --")
    print(full[col].value_counts(dropna=True).to_string())
    print()

print("DEPARTAMENTO vs DEPARTAMENTAL (constante esperada por archivo):")
crosscheck = full.groupby('__BASE__').apply(lambda g: sorted(g['DEPARTAMENTAL'].dropna().unique().tolist()))
print(crosscheck.to_string())

print()
print("="*70)
print("7. FORMATOS INCONSISTENTES")
print("="*70)

# DISTRITO formatos
def distrito_formato(x):
    if pd.isna(x) or x == '':
        return 'vacio'
    if re.fullmatch(r'\d{2}-\d{3}', x):
        return 'NN-NNN'
    if re.fullmatch(r'\d{2}-\d{2}-\d{4}', x):
        return 'NN-NN-NNNN'
    return 'otro/anomalo'

full['__DISTRITO_FMT__'] = full['DISTRITO'].apply(distrito_formato)
print("Formatos de DISTRITO:")
print(full['__DISTRITO_FMT__'].value_counts().to_string())
print("Ejemplos 'otro/anomalo':", full.loc[full['__DISTRITO_FMT__']=='otro/anomalo','DISTRITO'].unique()[:10])

# CODIGO formato
codigo_ok = full['CODIGO'].str.fullmatch(r'\d{2}-\d{2}-\d{4}-\d{2}').sum()
print("\nCODIGO conforme al patron NN-NN-NNNN-NN:", codigo_ok, "de", len(full))

# TELEFONO: cantidad de digitos, multiples numeros
def solo_digitos(x):
    if pd.isna(x):
        return None
    return re.sub(r'\D', '', x)

full['__TEL_DIGITOS__'] = full['TELEFONO'].apply(solo_digitos)
full['__TEL_LEN__'] = full['__TEL_DIGITOS__'].apply(lambda x: len(x) if isinstance(x, str) else None)
print("\nDistribucion de cantidad de digitos en TELEFONO:")
print(full['__TEL_LEN__'].value_counts(dropna=True).sort_index().to_string())
print("Telefonos con separador multiple (guion doble numero):",
      full['TELEFONO'].dropna().str.contains(r'\d-\d.*-\d|\d{6,}-\d{6,}').sum())

# espacios dobles / extremos
for col in ['ESTABLECIMIENTO','DIRECCION','SUPERVISOR_DIRECTOR','MUNICIPIO']:
    dobles = full[col].dropna().str.contains(r'  ').sum()
    extremos = full[col].dropna().apply(lambda x: x != x.strip()).sum()
    print(f"{col}: espacios dobles={dobles}, espacios extremos={extremos}")

print()
print("="*70)
print("8. PLACEHOLDERS Y ANOMALIAS")
print("="*70)
for col in ['SUPERVISOR_DIRECTOR','TELEFONO','DIRECCION','MUNICIPIO','ESTABLECIMIENTO']:
    ph = full[full[col].astype(str).str.fullmatch(r'-+') == True]
    if len(ph):
        print(f"{col}: {len(ph)} placeholders tipo guiones -> CODIGOs: {ph['CODIGO'].tolist()[:10]}")

print()
print("="*70)
print("9. RESUMEN POR BASE")
print("="*70)
resumen = full.groupby('__BASE__').apply(
    lambda g: pd.Series({
        'registros': len(g),
        'variables': len(cols),
        'dup_exactos': g[cols].duplicated().sum(),
        'pct_faltantes_global': round(g[cols].isna().sum().sum() / (len(g)*len(cols)) * 100, 2)
    })
)
print(resumen.to_string())

salida = os.path.join(DATA, "consolidado_grupoB.csv")
full.to_csv(salida, index=False, encoding="utf-8-sig")
print("\nConsolidado guardado en:", os.path.relpath(salida, BASE))
