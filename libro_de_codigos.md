LIBRO DE CÓDIGOS — ESTABLECIMIENTOS EDUCATIVOS DE NIVEL DIVERSIFICADO

PROYECTO 1 · CC3084 DATA SCIENCE · UNIVERSIDAD DEL VALLE DE GUATEMALA · SEMESTRE II 2026

__ METADATOS DEL CONJUNTO DE DATOS ______________________________________________

| Campo                       | Valor                                                       |

| Descripción                 | Establecimientos educativos de Guatemala que llegan hasta
                                el nivel diversificado (NIVEL ESCOLAR: DIVERSIFICADO), de
                                LOS 22 DEPARTAMENTOS DEL PAÍS.                              |
| Fuente de los datos         | Ministerio de Educación de Guatemala (MINEDUC) — Buscador de establecimientos: http://www.mineduc.gob.gt/BUSCAESTABLECIMIENTO_GE/ |
| Fecha de extracción         | Julio 2026 |
| Fecha de limpieza           | Julio 2026 |
| Versión del conjunto limpio | v1.0 |
| Archivo limpio              | `Data/limpio/establecimientos_diversificado_limpio.csv` |
| Codificación                | UTF-8 con BOM |
| Registros                   | 9,706 |
| Variables                   | 22 |
| Cobertura                   | 22 departamentos de Guatemala (país completo) |
| Llave primaria              | `CODIGO` (única, sin repetidos) |

ORIGEN DE LOS DATOS CRUDOS

Los datos crudos vinieron en 22 archivos CSV (uno por departamento), en dos estructuras distintas:

- Grupo A (11 archivos `<depto>diversificado.csv`): 4,033 registros, 18 columnas, UTF-8 con BOM, con `SUPERVISOR` y `DIRECTOR` separados y una columna sin nombre 100 % vacía.
- Grupo B (11 archivos `<depto>_diversificado_limpio.csv`): 5,673 registros, 16 columnas, UTF-8 sin BOM, con `SUPERVISOR_DIRECTOR` fusionado y un desplazamiento de columnas hacia `DEPARTAMENTAL`.


! LA LIMPIEZA UNIFICÓ AMBOS GRUPOS EN UN SOLO CONJUNTO CON ESTRUCTURA CONSISTENTE. EL PROCESO COMPLETO Y REPRODUCIBLE ESTÁ EN `CODE/LIMPIEZA.IPYNB` (USA `CODE/LIMPIEZA_LIB.PY`).




__ DICCIONARIO DE VARIABLES _____________________________________________________

Notación de tipo: texto, categórico, entero, booleano.

1. CODIGO
- Descripción: Código único del establecimiento asignado por el MINEDUC.
- Tipo de dato: texto.
- Dominio permitido: patrón `NN-NN-NNNN-NN`.
- Valores posibles: 9,706 valores únicos.
- Tratamiento aplicado: ninguno; se verificó formato y unicidad (Es la llave primaria).
- Faltantes: 0 %.

2. DISTRITO
- Descripción: Código del distrito educativo al que pertenece el establecimiento.
- Tipo de dato: texto (código).
- Dominio permitido: `NN-NN-NNNN` o `NN-NNN`.
- Valores posibles: 1,590 códigos.
- Tratamiento aplicado: se conservaron los dos formatos válidos; los códigos truncados imposibles (`17-`, `10-`) se convirtieron a NA (3 registros).
- Faltantes: 3.27 %.

3. DEPARTAMENTO
- Descripción: Departamento de Guatemala donde se ubica el establecimiento.
- Tipo de dato: categórico.
- Dominio permitido: los 22 departamentos oficiales de Guatemala.
- Valores posibles: ALTA VERAPAZ, BAJA VERAPAZ, CHIMALTENANGO, CHIQUIMULA, EL PROGRESO, ESCUINTLA, GUATEMALA, HUEHUETENANGO, IZABAL, JALAPA, JUTIAPA, PETEN, QUETZALTENANGO, QUICHE, RETALHULEU, SACATEPEQUEZ, SAN MARCOS, SANTA ROSA, SOLOLA, SUCHITEPEQUEZ, TOTONICAPAN, ZACAPA.
- Tratamiento aplicado: mayúsculas y sin tildes (criterio unificado).
- Faltantes: 0 %.

4. MUNICIPIO
- Descripción: Municipio donde se ubica el establecimiento.
- Tipo de dato: categórico.
- Dominio permitido: municipios de Guatemala pertenecientes al departamento correspondiente.
- Valores posibles: 505 municipios.
- Tratamiento aplicado: normalización de texto (mayúsculas, espacios, invisibles).
- Faltantes: 0 %.

5. ESTABLECIMIENTO
- Descripción: Nombre oficial del establecimiento educativo.
- Tipo de dato: texto libre.
- Dominio permitido: texto.
- Valores posibles: 5,552 nombres únicos.
- Tratamiento aplicado: mayúsculas, eliminación de espacios dobles e invisibles, corrección de acento grave invertido (`Ò`→`Ó`). No se alteraron los nombres oficiales.
- Faltantes: 1.13 %.

6. DIRECCION
- Descripción: Dirección física del establecimiento.
- Tipo de dato: texto libre.
- Dominio permitido: texto.
- Valores posibles: 5,490 direcciones únicas.
- Tratamiento aplicado: normalización de texto. En el Grupo B algunos registros traían datos mezclados de otros campos; solo se corrigió con evidencia suficiente y se conservaron nulos cuando no fue posible recuperar el dato.
- Faltantes: 6.62 %.

7. TELEFONO
- Descripción: Teléfono(s) del establecimiento tal como vino en la fuente (respaldo crudo normalizado).
- Tipo de dato: texto (puede contener más de un número).
- Dominio permitido: texto con dígitos y separadores.
- Tratamiento aplicado: normalización de texto. Se conserva como respaldo; los valores usables se derivan en `TELEFONO_1`/`TELEFONO_2`.
- Faltantes: 7.10 %.

8. TELEFONO_1 (variable derivada)
- Descripción: Primer número telefónico válido extraído de `TELEFONO`.
- Tipo de dato: texto (8 dígitos).
- Dominio permitido: exactamente 8 dígitos (estándar de Guatemala).
- Tratamiento aplicado: se separó `TELEFONO` por sus distintos separadores (guion, espacio, coma) y se tomó el primer número de 8 dígitos.
- Faltantes: 7.68 %.

9. TELEFONO_2 (variable derivada)
- Descripción: Segundo número telefónico válido, cuando el registro tenía más de uno.
- Tipo de dato: texto (8 dígitos).
- Dominio permitido: exactamente 8 dígitos.
- Tratamiento aplicado: igual que `TELEFONO_1`, tomando el segundo número válido.
- Faltantes: 99.11 % (solo aplica a registros con dos teléfonos).

10. N_TELEFONOS (variable derivada)
- Descripción: Cantidad de números telefónicos válidos (8 dígitos) encontrados en el registro.
- Tipo de dato: entero.
- Dominio permitido: 0, 1, 2, 3.
- Utilidad: permite validar formato y detectar registros sin teléfono válido.
- Faltantes: 0 %.

11. SUPERVISOR_DIRECTOR
- Descripción: Nombre del supervisor y/o director del establecimiento.
- Tipo de dato: texto libre.
- Dominio permitido: texto (nombres de persona).
- Valores posibles: 6,136 valores únicos.
- Tratamiento aplicado: en el Grupo A se fusionaron las columnas `SUPERVISOR` y `DIRECTOR` (separadas por espacio) para uniformar con el Grupo B, que ya venía fusionado. El marcador `----` se convirtió a NA. No se intentó separar los dos nombres en el Grupo B por falta de un delimitador confiable.
- Faltantes: 5.75 %.

12. NIVEL
- Descripción: Nivel educativo del establecimiento.
- Tipo de dato: categórico (constante).
- Dominio permitido: DIVERSIFICADO.
- Valores posibles: DIVERSIFICADO (único valor).
- Tratamiento aplicado: se conserva como constante documentada; confirma el filtro de extracción (solo nivel diversificado).
- Faltantes: 0 %.

13. SECTOR
- Descripción: Sector administrativo del establecimiento.
- Tipo de dato: categórico.
- Dominio permitido: OFICIAL, PRIVADO, COOPERATIVA, MUNICIPAL.
- Tratamiento aplicado: mayúsculas, sin tildes.
- Faltantes: 0 %.

14. AREA
- Descripción: Área geográfica del establecimiento.
- Tipo de dato: categórico.
- Dominio permitido: URBANA, RURAL.
- Tratamiento aplicado: mayúsculas, sin tildes.
- Faltantes: 0.02 % (2 registros).

15. STATUS
- Descripción: Estado operativo del establecimiento.
- Tipo de dato: categórico.
- Dominio permitido: ABIERTA, CERRADA TEMPORALMENTE, CERRADA DEFINITIVAMENTE, TEMPORAL NOMBRAMIENTO, TEMPORAL TITULOS.
- Tratamiento aplicado: en el Grupo B se recuperó desde `DEPARTAMENTAL` por el desplazamiento de columnas; mayúsculas, sin tildes.
- Faltantes: 0 % (2 registros marcados en REVISAR_MANUAL).

16. MODALIDAD
- Descripción: Modalidad lingüística del establecimiento.
- Tipo de dato: categórico.
- Dominio permitido: MONOLINGUE, BILINGUE.
- Tratamiento aplicado: recuperación desde `DEPARTAMENTAL` (Grupo B); mayúsculas, sin tildes.
- Faltantes: 0 %.

17. JORNADA
- Descripción: Jornada en la que opera el establecimiento.
- Tipo de dato: categórico.
- Dominio permitido: MATUTINA, VESPERTINA, DOBLE, NOCTURNA, INTERMEDIA, SIN JORNADA.
- Tratamiento aplicado: recuperación desde `DEPARTAMENTAL` (Grupo B); mayúsculas, sin tildes.
- Faltantes: 0 %.

18. PLAN
- Descripción: Plan de estudios del establecimiento.
- Tipo de dato: categórico.
- Dominio permitido: DIARIO(REGULAR), FIN DE SEMANA, SABATINO, DOMINICAL, MIXTO, IRREGULAR, A DISTANCIA, VIRTUAL A DISTANCIA, SEMIPRESENCIAL, SEMIPRESENCIAL (FIN DE SEMANA), SEMIPRESENCIAL (UN DIA A LA SEMANA), SEMIPRESENCIAL (DOS DIAS A LA SEMANA).
- Tratamiento aplicado: recuperación desde `DEPARTAMENTAL` (Grupo B); mayúsculas, sin tildes.
- Faltantes: 0.02 %.

19. DEPARTAMENTAL
- Descripción: Dirección departamental que supervisa el establecimiento (jurisdicción administrativa del MINEDUC).
- Tipo de dato: categórico.
- Dominio permitido: los 22 departamentos, con estas subdivisiones legítimas: GUATEMALA se divide en GUATEMALA NORTE, SUR, ORIENTE y OCCIDENTE; QUICHE se divide en QUICHE y QUICHE NORTE. (26 jurisdicciones en total.)
- Tratamiento aplicado: en el Grupo B se extrajo la jurisdicción del texto contaminado por el desplazamiento de columnas; mayúsculas, sin tildes.
- Faltantes: 0 %.

20. GRUPO_ORIGEN (variable derivada)
- Descripción: Grupo estructural del archivo crudo del que proviene el registro.
- Tipo de dato: categórico.
- Dominio permitido: A, B.
- Utilidad: trazabilidad del origen y de las decisiones de limpieza específicas por grupo.
- Faltantes: 0 %.

21. ES_POSIBLE_DUPLICADO (variable derivada)
- Descripción: Indica si el registro forma parte de un par de posibles duplicados parciales.
- Tipo de dato: booleano.
- Dominio permitido: True, False.
- Cómo se calculó: dos registros del mismo departamento y municipio con nombre casi idéntico (RapidFuzz token_sort_ratio ≥ 90), misma dirección (≥ 90) o mismo teléfono, y coincidencia en JORNADA, PLAN SECTOR y AREA.
- Utilidad: marca 1,724 filas (1,030 pares) para revisión. No se eliminaron: `CODIGO` es llave única oficial y representan inscripciones distintas. El detalle está en `Data/limpio/posibles_duplicados.csv`.
- Faltantes: 0 %.

22. REVISAR_MANUAL (variable derivada)
- Descripción: Motivo por el que un registro no pudo resolverse de forma totalmente automática.
- Tipo de dato: texto.
- Dominio permitido: texto o NA.
- Utilidad: marca los 4 registros del Grupo B cuyo desplazamiento de columnas dejó texto sin asignar tras el parseo. Se conservan con la jurisdicción ya extraída y una nota para revisión.
- Faltantes: 99.96 % (solo 4 registros tienen valor).





VARIABLES DERIVADAS (RESUMEN)

| Variable                   | Se creó porque                                    | Cómo se calculó                                                 | Utilidad |

| `TELEFONO_1`, `TELEFONO_2` | El campo original mezclaba varios teléfonos       | Separando `TELEFONO` por sus separadores y validando 8 dígitos  | Un teléfono por columna, validable |
| `N_TELEFONOS`              | Se necesita saber cuántos teléfonos válidos hay   | Conteo de números de 8 dígitos por registro                     | Validación y control de calidad |
| `GRUPO_ORIGEN`             | Los datos vinieron en dos estructuras             | Etiqueta A/B según el archivo de origen                         | Trazabilidad |
| `ES_POSIBLE_DUPLICADO`     | La guía exige detectar duplicados parciales       | Similitud de cadenas (RapidFuzz) + coincidencia de campos clave | Revisión de duplicados sin borrado automático |
| `REVISAR_MANUAL`           | Algunos casos no se resuelven sin criterio humano | Marca puesta durante la reparación del desplazamiento           | Auditoría y revisión manual |

REPRODUCIBILIDAD

La raíz del repositorio:

pip install pandas numpy rapidfuzz unidecode nbformat nbconvert ipykernel
PYTHON -M NBCONVERT --TO NOTEBOOK --EXECUTE --INPLACE CODE/LIMPIEZA.IPYNB

GENERA EL:
`DATA/LIMPIO/ESTABLECIMIENTOS_DIVERSIFICADO_LIMPIO.CSV`
Y LOS REPORTES DE APOYO:
(`REGISTRO_TRANSFORMACIONES.CSV`, `INFORME_CALIDAD.CSV`, `POSIBLES_DUPLICADOS.CSV`).