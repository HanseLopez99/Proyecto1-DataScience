DIAGNOSTICO DEL CONJUNTO DE DATOS
ESTABLECIMIENTOS EDUCATIVOS HASTA NIVEL DIVERSIFICADO - 22 DEPARTAMENTOS DE GUATEMALA
NOTA PREVIA: SON DOS GRUPOS CON ESTRUCTURA DISTINTA

- GRUPO A: 11 archivos originales, 18 columnas, UTF-8 CON BOM.
  Archivos: <departamento> + diversificado.csv
  Departamentos: peten, quetzaltenango, quiche, retalhuleu, sacatepequez,
  sanmarcos, santarosa, solola, suchitepequez, totonicapan, zacapa.

- GRUPO B: 11 archivos, 16 columnas, UTF-8 SIN BOM.
  Archivos: <departamento> + _diversificado_limpio.csv
  Departamentos: alta_verapaz, baja_verapaz, chimaltenango, chiquimula,
  el_progreso, escuintla, guatemala, huehuetenango, izabal, jalapa, jutiapa.

- Dentro de cada grupo la estructura es identica. Entre grupos no.
- Por eso cada inciso se responde por separado para A y para B.


1. NUMERO DE REGISTROS Y VARIABLES

- Grupo A: 4033 registros, 18 variables, 11 archivos.
- Grupo B: 5673 registros, 16 variables, 11 archivos.
- Total: 9706 registros, 22 archivos, 22 departamentos.

Registros por archivo, grupo A:
- sanmarcos: 724
- quetzaltenango: 551
- peten: 516
- suchitepequez: 437
- sacatepequez: 430
- retalhuleu: 364
- quiche: 322
- santarosa: 213
- solola: 192
- zacapa: 156
- totonicapan: 128

Registros por archivo, grupo B:
- guatemala: 1908
- escuintla: 708
- huehuetenango: 591
- alta_verapaz: 475
- chimaltenango: 435
- izabal: 413
- jutiapa: 392
- chiquimula: 239
- jalapa: 183
- baja_verapaz: 171
- el_progreso: 158


2. TIPO DE DATO DE CADA VARIABLE

Las 22 bases leen todas sus columnas como texto (string). Ninguna variable
es numerica. El tipo listado es la naturaleza real del contenido.

Grupo A (18 variables):
- CODIGO: texto, identificador
- (columna sin nombre, posicion 1): vacia, 0 valores
- DISTRITO: texto, codigo
- DEPARTAMENTO: texto, categorico
- MUNICIPIO: texto, categorico
- ESTABLECIMIENTO: texto libre
- DIRECCION: texto libre
- TELEFONO: texto, numerico no convertible a entero
- SUPERVISOR: texto libre, nombre de persona
- DIRECTOR: texto libre, nombre de persona
- NIVEL: texto, categorico constante
- SECTOR: texto, categorico
- AREA: texto, categorico
- STATUS: texto, categorico
- MODALIDAD: texto, categorico
- JORNADA: texto, categorico
- PLAN: texto, categorico
- DEPARTAMENTAL: texto, categorico

Grupo B (16 variables):
- CODIGO: texto, identificador
- DISTRITO: texto, codigo
- DEPARTAMENTO: texto, categorico
- MUNICIPIO: texto, categorico
- ESTABLECIMIENTO: texto libre
- DIRECCION: texto libre
- TELEFONO: texto, numerico no convertible a entero
- SUPERVISOR_DIRECTOR: texto libre, DOS nombres de persona concatenados
- NIVEL: texto, categorico constante
- SECTOR: texto, categorico
- AREA: texto, categorico
- STATUS: texto, categorico
- MODALIDAD: texto, categorico
- JORNADA: texto, categorico
- PLAN: texto, categorico
- DEPARTAMENTAL: texto, categorico contaminado (ver inciso 6)

Aclaraciones de tipo:
- TELEFONO no se puede convertir a entero: hay celdas con dos telefonos
  separados por guion, espacio o coma.
- El grupo B no tiene la columna sin nombre que si tiene el grupo A.
- El grupo B fusiona SUPERVISOR y DIRECTOR en una sola columna.


3. CANTIDAD Y PORCENTAJE DE VALORES FALTANTES POR VARIABLE

Grupo A, base 4033 registros:
- (columna sin nombre): 4033 faltantes, 100.00%
- DIRECTOR: 475 faltantes, 11.78%
- TELEFONO: 295 faltantes, 7.31%
- SUPERVISOR: 118 faltantes, 2.93%
- DISTRITO: 115 faltantes, 2.85%
- DIRECCION: 39 faltantes, 0.97%
- ESTABLECIMIENTO: 1 faltante, 0.02%
- CODIGO: 0 faltantes, 0.00%
- DEPARTAMENTO: 0 faltantes, 0.00%
- MUNICIPIO: 0 faltantes, 0.00%
- NIVEL: 0 faltantes, 0.00%
- SECTOR: 0 faltantes, 0.00%
- AREA: 0 faltantes, 0.00%
- STATUS: 0 faltantes, 0.00%
- MODALIDAD: 0 faltantes, 0.00%
- JORNADA: 0 faltantes, 0.00%
- PLAN: 0 faltantes, 0.00%
- DEPARTAMENTAL: 0 faltantes, 0.00%

Grupo B, base 5673 registros:
- PLAN: 817 faltantes, 14.40%
- JORNADA: 638 faltantes, 11.25%
- DIRECCION: 600 faltantes, 10.58%
- SUPERVISOR_DIRECTOR: 449 faltantes, 7.91%
- TELEFONO: 394 faltantes, 6.95%
- DISTRITO: 199 faltantes, 3.51%
- ESTABLECIMIENTO: 109 faltantes, 1.92%
- STATUS: 55 faltantes, 0.97%
- MODALIDAD: 55 faltantes, 0.97%
- AREA: 2 faltantes, 0.04%
- CODIGO: 0 faltantes, 0.00%
- DEPARTAMENTO: 0 faltantes, 0.00%
- MUNICIPIO: 0 faltantes, 0.00%
- NIVEL: 0 faltantes, 0.00%
- SECTOR: 0 faltantes, 0.00%
- DEPARTAMENTAL: 0 faltantes, 0.00%

Datos puntuales:
- ESTABLECIMIENTO faltante en A: CODIGO 11-05-1304-46
- AREA faltante en B: CODIGO 16-01-0982-46 y 05-02-0065-46
- De los faltantes de B, 1565 no son perdida real (PLAN 817 + JORNADA 638 +
  STATUS 55 + MODALIDAD 55): estan dentro de DEPARTAMENTAL, ver inciso 6.
- Faltantes disfrazados: 3 registros de DIRECTOR en A tienen "----" en vez
  de vacio, no se cuentan como nulos arriba.
- Concentracion: en A los faltantes se reparten parejo entre departamentos.
  En B, guatemala es el que mas aporta por ser el archivo mas grande, y
  huehuetenango tiene 242 de las 600 direcciones vacias.


4. CANTIDAD DE VALORES UNICOS

Grupo A:
- CODIGO: 4033
- (columna sin nombre): 0
- DISTRITO: 753
- DEPARTAMENTO: 11
- MUNICIPIO: 182
- ESTABLECIMIENTO: 2102
- DIRECCION: 2448
- TELEFONO: 2339
- SUPERVISOR: 598
- DIRECTOR: 2065
- NIVEL: 1
- SECTOR: 4
- AREA: 2
- STATUS: 5
- MODALIDAD: 2
- JORNADA: 6
- PLAN: 12
- DEPARTAMENTAL: 12

Grupo B:
- CODIGO: 5673
- DISTRITO: 841
- DEPARTAMENTO: 11
- MUNICIPIO: 331
- ESTABLECIMIENTO: 3489
- DIRECCION: 3093
- TELEFONO: 3207
- SUPERVISOR_DIRECTOR: 3553
- NIVEL: 1
- SECTOR: 4
- AREA: 2
- STATUS: 3
- MODALIDAD: 2
- JORNADA: 5
- PLAN: 5
- DEPARTAMENTAL: 120

Lecturas de estos numeros:
- CODIGO tiene tantos unicos como registros en ambos grupos: es llave unica.
- NIVEL tiene 1 unico en ambos grupos: es constante.
- DEPARTAMENTAL en B tiene 120 unicos cuando deberia tener 14: esta roto.
- STATUS, JORNADA y PLAN tienen menos unicos en B que en A porque B perdio
  categorias, ver inciso 6.


5. CANTIDAD DE REGISTROS DUPLICADOS EXACTOS

- Grupo A: 0 duplicados exactos.
- Grupo B: 0 duplicados exactos.
- Total: 0 duplicados exactos en los 22 archivos.
- CODIGO repetidos en A: 0.
- CODIGO repetidos en B: 0.
- CODIGO presentes en ambos grupos a la vez: 0, no hay traslape.
- Conclusion: CODIGO es llave primaria valida, 4033 unicos en A y 5673 en B.


6. VARIABLES CON VALORES FUERA DE DOMINIO O INCONSISTENTES

6.1 DEPARTAMENTAL en el grupo B: 817 registros contaminados
- Es el problema mas grave del conjunto.
- Tiene 120 valores unicos cuando deberia tener 14.
- Los valores de STATUS, MODALIDAD, JORNADA y PLAN se corrieron y quedaron
  pegados dentro del texto de DEPARTAMENTAL.
- Ejemplos reales del valor de DEPARTAMENTAL:
  "SIN JORNADA SEMIPRESENCIAL (FIN DE SEMANA) GUATEMALA SUR"
  "A DISTANCIA GUATEMALA OCCIDENTE"
  "SEMIPRESENCIAL ALTA VERAPAZ"
  "IRREGULAR IZABAL"
  "INTERCALADO HUEHUETENANGO"
  "TEMPORAL TITULOS MONOLINGUE VESPERTINA DIARIO(REGULAR) GUATEMALA SUR"
  "SIN ESPECIFICAR CERRADA TEMPORALMENTE MONOLINGUE DOBLE SEMIPRESENCIAL ALTA VERAPAZ"
- Prueba: los 817 registros con DEPARTAMENTAL contaminado son exactamente
  los mismos 817 que tienen PLAN vacio. En las filas con DEPARTAMENTAL
  limpio hay 0 faltantes de JORNADA y 0 de PLAN.
- La informacion no se perdio, esta en la columna equivocada. Es recuperable.
- Las 14 jurisdicciones validas de DEPARTAMENTAL en B: GUATEMALA SUR,
  GUATEMALA OCCIDENTE, GUATEMALA ORIENTE, GUATEMALA NORTE, ESCUINTLA,
  HUEHUETENANGO, ALTA VERAPAZ, CHIMALTENANGO, IZABAL, JUTIAPA, CHIQUIMULA,
  JALAPA, BAJA VERAPAZ, EL PROGRESO

6.2 Categorias que el grupo B perdio por el corrimiento
- STATUS perdio: TEMPORAL NOMBRAMIENTO, TEMPORAL TITULOS
- JORNADA perdio: SIN JORNADA
- PLAN perdio: SEMIPRESENCIAL y sus 3 variantes, A DISTANCIA,
  VIRTUAL A DISTANCIA, IRREGULAR
- Todas esas categorias si existen en el grupo A.
- Aparecen ademas dos categorias que no existen en A: "SIN ESPECIFICAR"
  (de STATUS) e "INTERCALADO" (de JORNADA).

6.3 NIVEL: constante en los dos grupos
- Unico valor "DIVERSIFICADO": 4033 en A, 5673 en B.
- No sirve para diferenciar registros.

6.4 DIRECTOR en el grupo A: placeholder "----"
- 3 registros usan "----" en vez de un nombre real.
- CODIGO afectados: 17-01-0035-46, 09-01-0040-46, 10-10-0049-46
- SUPERVISOR no tiene este marcador.

6.5 TELEFONO: valores fuera del estandar de 8 digitos de Guatemala
- Grupo A: 3695 correctos, 43 fuera de estandar.
  Digitos encontrados: 1, 5, 6, 7, 8, 12, 14, 15, 16 y 24.
- Grupo B: 5179 correctos, 100 fuera de estandar.
  Digitos encontrados: 7, 8, 12, 14 y 16.
- Los de mas de 8 digitos son celdas con dos telefonos. Los de menos son
  numeros incompletos.

6.6 SUPERVISOR_DIRECTOR en el grupo B: dos personas en un campo
- Concatena supervisor y director SIN separador, en 5224 registros.
- Ejemplos reales:
  "JOSE ARTURO CHOC CHEN GUSTAVO ADOLFO SIERRA POP"
  "DAVID SOTOJ SANCHEZ OLGA LETICIA PEREZ GARICA"
- No es separable de forma automatica confiable: no hay delimitador y los
  nombres tienen cantidad variable de palabras.

6.7 PLAN en el grupo A: dominio fragmentado
- SEMIPRESENCIAL, SEMIPRESENCIAL (FIN DE SEMANA), SEMIPRESENCIAL (UN DIA A
  LA SEMANA) y SEMIPRESENCIAL (DOS DIAS A LA SEMANA) son 4 categorias
  separadas.
- Categorias de frecuencia minima: MIXTO 2, IRREGULAR 1.

6.8 DEPARTAMENTAL no tiene relacion 1 a 1 con DEPARTAMENTO
- En A: QUICHE se parte en QUICHE (261) y QUICHE NORTE (61).
- En B: GUATEMALA se parte en NORTE, SUR, ORIENTE y OCCIDENTE.
- No es un error: son jurisdicciones administrativas reales.

6.9 Dominios completos, para verificar contra la fuente
- NIVEL en A: DIVERSIFICADO 4033
- NIVEL en B: DIVERSIFICADO 5673
- SECTOR en A: PRIVADO 3165, OFICIAL 633, COOPERATIVA 177, MUNICIPAL 58
- SECTOR en B: PRIVADO 4712, OFICIAL 725, MUNICIPAL 118, COOPERATIVA 118
- AREA en A: URBANA 3042, RURAL 991
- AREA en B: URBANA 4271, RURAL 1400, vacio 2
- MODALIDAD en A: MONOLINGUE 3817, BILINGUE 216
- MODALIDAD en B: MONOLINGUE 5369, BILINGUE 249, vacio 55
- STATUS en A: ABIERTA 2524, CERRADA TEMPORALMENTE 901,
  CERRADA DEFINITIVAMENTE 570, TEMPORAL NOMBRAMIENTO 21, TEMPORAL TITULOS 17
- STATUS en B: ABIERTA 3514, CERRADA TEMPORALMENTE 1389,
  CERRADA DEFINITIVAMENTE 715, vacio 55
- JORNADA en A: VESPERTINA 1403, DOBLE 1338, MATUTINA 778, SIN JORNADA 369,
  NOCTURNA 119, INTERMEDIA 26
- JORNADA en B: DOBLE 1871, VESPERTINA 1659, MATUTINA 1295, NOCTURNA 172,
  INTERMEDIA 38, vacio 638
- PLAN en A: DIARIO(REGULAR) 2619, FIN DE SEMANA 933,
  SEMIPRESENCIAL (UN DIA A LA SEMANA) 189, SEMIPRESENCIAL (FIN DE SEMANA) 159,
  A DISTANCIA 54, VIRTUAL A DISTANCIA 24, SEMIPRESENCIAL 21, DOMINICAL 13,
  SABATINO 11, SEMIPRESENCIAL (DOS DIAS A LA SEMANA) 7, MIXTO 2, IRREGULAR 1
- PLAN en B: DIARIO(REGULAR) 3372, FIN DE SEMANA 1460, SABATINO 18,
  DOMINICAL 5, MIXTO 1, vacio 817
- DEPARTAMENTO en A: 11 valores, sin tildes
- DEPARTAMENTO en B: 11 valores, sin tildes
- DEPARTAMENTAL en A: 12 valores, con tildes
- DEPARTAMENTAL en B: 120 valores, roto


7. VARIABLES CON FORMATOS INCONSISTENTES

7.1 DISTRITO: dos formatos de codigo mezclados, en los dos grupos
- Formato NN-NN-NNNN, ejemplo 09-01-0424: 2350 en A, 3111 en B
- Formato NN-NNN, ejemplo 17-001: 1565 en A, 2363 en B
- Valores truncados en A, solo el prefijo: "17-" y "10-" (2 registros)
- Valores truncados en B: 0

7.2 TELEFONO: separadores inconsistentes entre multiples numeros
- Separadores encontrados: guion, espacio y coma.
- Ejemplos reales del grupo A:
  "31193946-46843572"
  "66502390 65864538"
  "7618119, 7619218"
  "7631022-7615248"
- Ejemplos reales del grupo B:
  "78208583-78209143"
  "23661344-23661600"
  "79649696-78739432"
- Numeros incompletos: "4085613" (7 digitos), "586577" (6 digitos)

7.3 Acentuacion inconsistente
- DEPARTAMENTO va SIN tildes en los dos grupos: PETEN, QUICHE, SOLOLA.
- DEPARTAMENTAL va CON tildes en el grupo A: PETÉN, QUICHÉ, SOLOLÁ.
- DEPARTAMENTAL va SIN tildes en el grupo B.
- Es el mismo dato escrito con dos criterios distintos.

7.4 Encoding distinto entre grupos
- Grupo A: UTF-8 CON BOM.
- Grupo B: UTF-8 SIN BOM.
- Leer todo con encoding="utf-8-sig" funciona para los dos casos.

7.5 Espacios dobles internos
- Grupo A: 0 casos en todas las columnas de texto.
- Grupo B: 11 casos en ESTABLECIMIENTO, 3 en DIRECCION.
- Ejemplo: "CENTRO EDUCATIVO  EL PROGRESO 5A."

7.6 Errores de digitacion
- Tilde invertida: "EDUCACIÒN" donde corresponde "EDUCACIÓN".

7.7 CODIGO: sin problema de formato
- Los 9706 valores cumplen el patron NN-NN-NNNN-NN, 100% conforme.
- 0 fuera de patron en A y 0 en B.

7.8 Espacios al inicio o final de campo
- 0 casos en los dos grupos, en todas las columnas de texto.


8. PROBLEMAS POTENCIALES DE CALIDAD DE DATOS

Ordenados de mas grave a menos grave. La accion sugerida va al lado.

- P1. Columnas corridas en el grupo B, 817 registros. STATUS, MODALIDAD,
  JORNADA y PLAN quedaron dentro del texto de DEPARTAMENTAL. Causa raiz de
  1565 faltantes.
  Accion: parsear DEPARTAMENTAL de atras hacia adelante; el
  final de la cadena siempre es una de las 14 jurisdicciones validas y lo
  que sobra por delante son los valores de las otras 4 columnas.

- P2. Los dos grupos no son concatenables: 18 columnas contra 16, columna
  sin nombre solo en A, SUPERVISOR y DIRECTOR separados en A pero fusionados
  en B, BOM solo en A.
  Accion: borrar la columna vacia de A, decidir el criterio de SUPERVISOR/DIRECTOR, leer todo con utf-8-sig.

- P3. SUPERVISOR_DIRECTOR fusiona dos personas sin separador, 5224 registros
  del grupo B. No tiene arreglo automatico confiable.
  Accion: conseguir los
  archivos crudos de esos 11 departamentos, o fusionar tambien en A y
  aceptar la perdida.

- P4. Columna sin nombre en el grupo A: 100% vacia, 4033 celdas, 0 datos.
  Accion: borrarla.

- P5. Telefonos con dos numeros en una celda y numeros incompletos, 143 en
  total (43 en A, 100 en B).
  Accion: separar en TELEFONO_1 y TELEFONO_2 con los 3 separadores, marcar como invalido lo que no llegue a 8 digitos.

- P6. DISTRITO con dos formatos mezclados en los dos grupos, mas 2 valores
  truncados en A.
  Accion: estandarizar a un solo formato, corregir o anular los truncados.

- P7. Contaminacion entre ESTABLECIMIENTO y DIRECCION en el grupo B.
  Ejemplo, CODIGO 16-01-0137-46:
  ESTABLECIMIENTO = "INSTITUTO MIXTO NOCTURNO FRANCISCO MARROQUIN 6A."
  DIRECCION = "AVENIDA 1-15 ZONA 4 JORGE EDUARDO PAQUE LAZARO"
  El "6A." va con la direccion y el nombre de persona no deberia estar ahi.
  Accion: revisar caso por caso, no hay patron automatico.

- P8. Faltantes reales altos en A: DIRECTOR 11.78%, TELEFONO 7.31%,
  SUPERVISOR 2.93%, DISTRITO 2.85%.
  Accion: verificar contra la fuente.

- P9. Faltantes reales altos en B, ya descontado P1: DIRECCION 10.58%,
  SUPERVISOR_DIRECTOR 7.91%, TELEFONO 6.95%, DISTRITO 3.51%.
  Accion: verificar contra la fuente. huehuetenango concentra 242 de las 600 direcciones vacias.

- P10. Acentuacion inconsistente entre DEPARTAMENTO y DEPARTAMENTAL, y entre
  el grupo A y el grupo B.
  Accion: definir un criterio unico y aplicarlo.

- P11. Placeholder "----" en DIRECTOR del grupo A, 3 registros.
Accion: convertir a nulo real antes de contar faltantes.

- P12. NIVEL constante en los 22 archivos.
Accion: eliminar o documentar.

- P13. PLAN del grupo A con dominio fragmentado, 4 variantes de
  SEMIPRESENCIAL.
  Accion: agrupar categorias.

- P14. Espacios dobles internos en el grupo B, 14 casos.
Accion: normalizar.

Lo que esta bien y no hay que tocar:
- 0 registros duplicados exactos en los 22 archivos.
- 0 codigos repetidos y 0 traslape de CODIGO entre grupos.
- CODIGO cumple el formato NN-NN-NNNN-NN en el 100% de los 9706 registros.
- 0 espacios al inicio o final de los campos de texto.
- SECTOR y DEPARTAMENTO: sin faltantes y con dominios limpios en los 2 grupos.
- AREA, STATUS, MODALIDAD, JORNADA y PLAN: sin faltantes en el grupo A.
- La estructura es homogenea dentro de cada grupo.


NOTA FINAL

Los archivos "_limpio" del grupo B estan mas dañados que los originales del
grupo A. Vale la pena preguntar de donde salieron y si existe la version
cruda de esos 11 departamentos: recuperarlos desde la fuente es mas barato
que parsear las 817 cadenas de P1 y ademas resolveria P3, que no tiene
arreglo automatico confiable.
