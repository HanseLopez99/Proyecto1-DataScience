# Proyecto 1 — Obtención y Limpieza de Datos

**CC3084 Data Science · Universidad del Valle de Guatemala · Semestre II 2026**

Limpieza de los datos de establecimientos educativos de nivel diversificado de los
22 departamentos de Guatemala.
Fuente: [MINEDUC](http://www.mineduc.gob.gt/BUSCAESTABLECIMIENTO_GE/) · Extracción: julio 2026.

## Estructura del repositorio

```
Data/                                   Datos crudos (22 CSV, 2 grupos)
  <depto>diversificado.csv              Grupo A (11 archivos, 18 col)
  <depto>_diversificado_limpio.csv      Grupo B (11 archivos, 16 col)
  limpio/
    establecimientos_diversificado_limpio.csv   CONJUNTO LIMPIO FINAL (9,706 x 22)
    registro_transformaciones.csv       Tabla de transformaciones (act. 6)
    informe_calidad.csv                 Informe antes/después (act. 8)
    posibles_duplicados.csv             Duplicados parciales para revisión
code/
  diagnostico.py                        Diagnóstico de los datos crudos
  limpieza_lib.py                       Funciones reproducibles de limpieza
  limpieza.ipynb                        Pipeline de limpieza (act. 5–7)
  generar_libro_pdf.py                  Genera el libro de códigos en PDF
diagnostico_datos.md                    Diagnóstico del estado inicial (act. 3)
plan de limpieza.pdf                    Plan de limpieza por variable (act. 4)
libro_de_codigos.md                     Libro de códigos en markdown (act. 10)
libro_de_codigos.pdf                    Libro de códigos en PDF (act. 10)
```

## Reproducir la limpieza

Desde la raíz del repositorio:

```bash
pip install pandas numpy rapidfuzz unidecode nbformat nbconvert ipykernel
python -m nbconvert --to notebook --execute --inplace code/limpieza.ipynb
```

Esto regenera el conjunto limpio y todos los reportes en `Data/limpio/`.

## Resultados de la limpieza

| Métrica | Antes | Después |
|---|---|---|
| Registros | 9,706 | 9,706 |
| Variables | 19 | 22 |
| Valores faltantes | 15.97 % | 6.54 % |
| Duplicados exactos | 0 | 0 |
| Posibles duplicados parciales | — | 1,724 filas (conservadas, marcadas) |

Principal hallazgo: en el Grupo B, 817 registros tenían columnas desplazadas hacia
`DEPARTAMENTAL`; se recuperaron 1,563 valores devolviéndolos a su columna original.
