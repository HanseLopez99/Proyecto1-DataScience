DIAGNOSTICO DEL CONJUNTO DE DATOS
ESTABLECIMIENTOS EDUCATIVOS HASTA NIVEL DIVERSIFICADO - 22 DEPARTAMENTOS DE GUATEMALA


LO ESENCIAL EN 30 SEGUNDOS

  22 archivos CSV, 9706 registros, 22 departamentos.
  0 duplicados exactos. 0 codigos repetidos. CODIGO sirve como llave unica.

  Hay DOS grupos con estructura distinta. No se pueden juntar tal como estan.

  El problema mas grave: los 11 archivos "_limpio" tienen 817 registros con
  las columnas corridas. Empezar por ahi (problema 1).


A. LOS DOS GRUPOS

  GRUPO A - 11 archivos originales, 18 columnas, 4033 registros
    peten, quetzaltenango, quiche, retalhuleu, sacatepequez, sanmarcos,
    santarosa, solola, suchitepequez, totonicapan, zacapa
    Nombre de archivo: <departamento> + diversificado.csv
    Encoding: UTF-8 CON BOM

  GRUPO B - 11 archivos "_limpio", 16 columnas, 5673 registros
    alta_verapaz, baja_verapaz, chimaltenango, chiquimula, el_progreso,
    escuintla, guatemala, huehuetenango, izabal, jalapa, jutiapa
    Nombre de archivo: <departamento> + _diversificado_limpio.csv
    Encoding: UTF-8 SIN BOM


  Dentro de cada grupo la estructura es identica, pero entre grupos no.

  Las 3 diferencias entre A y B:
    1. A tiene una columna extra sin nombre en la posicion [1]. B no la tiene.
    2. A tiene SUPERVISOR y DIRECTOR separados. B los fusiona en una sola
       columna SUPERVISOR_DIRECTOR.
    3. A tiene BOM, B no.

  Columnas A (18): CODIGO, (sin nombre), DISTRITO, DEPARTAMENTO, MUNICIPIO,
    ESTABLECIMIENTO, DIRECCION, TELEFONO, SUPERVISOR, DIRECTOR, NIVEL,
    SECTOR, AREA, STATUS, MODALIDAD, JORNADA, PLAN, DEPARTAMENTAL

  Columnas B (16): CODIGO, DISTRITO, DEPARTAMENTO, MUNICIPIO,
    ESTABLECIMIENTO, DIRECCION, TELEFONO, SUPERVISOR_DIRECTOR, NIVEL,
    SECTOR, AREA, STATUS, MODALIDAD, JORNADA, PLAN, DEPARTAMENTAL

  Todas las columnas se leen como texto (string). Ninguna es numerica:
  TELEFONO parece numero pero tiene celdas con dos telefonos y guiones, no
  se puede convertir a entero.

  Registros por archivo:
    GRUPO A: sanmarcos 724, quetzaltenango 551, peten 516, suchitepequez 437,
      sacatepequez 430, retalhuleu 364, quiche 322, santarosa 213, solola 192,
      zacapa 156, totonicapan 128
    GRUPO B: guatemala 1908, escuintla 708, huehuetenango 591,
      alta_verapaz 475, chimaltenango 435, izabal 413, jutiapa 392,
      chiquimula 239, jalapa 183, baja_verapaz 171, el_progreso 158





B. PROBLEMAS A RESOLVER, EN ORDEN DE PRIORIDAD

PROBLEMA 1 - COLUMNAS CORRIDAS EN EL GRUPO B          817 de 5673 registros
  Que pasa: los valores de STATUS, MODALIDAD, JORNADA y PLAN se corrieron y
    quedaron pegados dentro del texto de DEPARTAMENTAL.
  Como se ve:
    DEPARTAMENTAL = "SIN JORNADA SEMIPRESENCIAL (FIN DE SEMANA) GUATEMALA SUR"
    DEPARTAMENTAL = "A DISTANCIA GUATEMALA OCCIDENTE"
    DEPARTAMENTAL = "TEMPORAL TITULOS MONOLINGUE VESPERTINA DIARIO(REGULAR) GUATEMALA SUR"
    ...y en esas mismas filas JORNADA y PLAN estan vacios.
  Prueba de que es esto y no otra cosa: los 817 registros con DEPARTAMENTAL
    contaminado son EXACTAMENTE los mismos 817 que tienen PLAN vacio. En las
    filas con DEPARTAMENTAL limpio hay 0 faltantes de JORNADA y 0 de PLAN.
  Consecuencia: DEPARTAMENTAL tiene 120 valores unicos cuando deberia tener 14.
  Buena noticia: la informacion NO se perdio, esta en la columna equivocada.
    Los 638 faltantes de JORNADA, 817 de PLAN, 55 de STATUS y 55 de MODALIDAD
    son RECUPERABLES parseando el texto de DEPARTAMENTAL.
  Que hacer: parsear DEPARTAMENTAL de atras hacia adelante. El final de la
    cadena es siempre una de las 14 jurisdicciones validas; lo que sobra por
    delante son los valores de STATUS / MODALIDAD / JORNADA / PLAN.
  Las 14 jurisdicciones validas de DEPARTAMENTAL en el grupo B:
    GUATEMALA SUR, GUATEMALA OCCIDENTE, GUATEMALA ORIENTE, GUATEMALA NORTE,
    ESCUINTLA, HUEHUETENANGO, ALTA VERAPAZ, CHIMALTENANGO, IZABAL, JUTIAPA,
    CHIQUIMULA, JALAPA, BAJA VERAPAZ, EL PROGRESO



PROBLEMA 2 - LOS DOS GRUPOS NO SON CONCATENABLES                 22 archivos
  Que hacer, en este orden:
    - Borrar la columna sin nombre del grupo A (esta 100% vacia, 0 datos).
    - Decidir que hacer con SUPERVISOR / DIRECTOR (ver problema 3).
    - Leer todo con encoding="utf-8-sig", asi funciona con y sin BOM.



PROBLEMA 3 - SUPERVISOR Y DIRECTOR FUSIONADOS EN EL GRUPO B         5224 reg
  Que pasa: SUPERVISOR_DIRECTOR mete dos personas distintas en un solo campo,
    concatenadas SIN separador.
  Como se ve:
    "JOSE ARTURO CHOC CHEN GUSTAVO ADOLFO SIERRA POP"
     ^--- supervisor ---^ ^------- director -------^
    "DAVID SOTOJ SANCHEZ OLGA LETICIA PEREZ GARICA"
  Ojo: NO se puede separar de forma automatica confiable. No hay delimitador
    y los nombres tienen cantidad variable de palabras.
  Que hacer, elegir una:
    a) Conseguir los archivos crudos de esos 11 departamentos (recomendado).
    b) Fusionar tambien SUPERVISOR + DIRECTOR en el grupo A para igualar, y
       aceptar la perdida de granularidad en los 22 archivos.

PROBLEMA 4 - TELEFONOS CON DOS NUMEROS EN UNA CELDA      143 reg (43 A, 100 B)
  Que pasa: celdas con mas de un telefono y separadores distintos, mas
    numeros incompletos.
  Como se ve:
    Dos numeros: "31193946-46843572"  "66502390 65864538"  "7618119, 7619218"
                 "78208583-78209143"  "23661344-23661600"
    Incompletos: "4085613" (7 digitos)  "586577" (6 digitos)
  Separadores encontrados: guion, espacio y coma.
  El estandar de Guatemala es 8 digitos. Distribucion real:
    Grupo A: 3695 con 8 digitos, 43 fuera de estandar (de 1 a 24 digitos)
    Grupo B: 5179 con 8 digitos, 100 fuera de estandar (7, 12, 14 y 16 digitos)
  Que hacer: separar en TELEFONO_1 y TELEFONO_2 usando los 3 separadores, y
    marcar como invalido lo que no llegue a 8 digitos.

PROBLEMA 5 - DISTRITO CON DOS FORMATOS MEZCLADOS                       todos
  Que pasa: conviven dos formatos de codigo sin criterio.
    Formato NN-NN-NNNN (ej. 09-01-0424): 2350 en A, 3111 en B
    Formato NN-NNN     (ej. 17-001)    : 1565 en A, 2363 en B
  Ademas: 2 valores truncados en el grupo A, solo el prefijo: "17-" y "10-"
  Faltantes: 115 en A (2.85%), 199 en B (3.51%)
  Que hacer: estandarizar a un solo formato y corregir o anular los 2 truncados.

PROBLEMA 6 - ACENTOS INCONSISTENTES                                    todos
  Que pasa: DEPARTAMENTO va SIN tildes en los dos grupos (PETEN, QUICHE,
    SOLOLA). Pero DEPARTAMENTAL va CON tildes en el grupo A (PETÉN, QUICHÉ,
    SOLOLÁ) y SIN tildes en el grupo B.
  Ademas: hay una tilde invertida, "EDUCACIÒN" donde va "EDUCACIÓN".
  Que hacer: definir un criterio unico (con o sin tildes) y aplicarlo a las
    dos columnas en los 22 archivos.

PROBLEMA 7 - FALTANTES DISFRAZADOS "----"                          3 registros
  Que pasa: la columna DIRECTOR del grupo A usa "----" (cuatro guiones) como
    placeholder. No es un nombre real pero tampoco se detecta como nulo.
  Registros afectados (CODIGO): 17-01-0035-46, 09-01-0040-46, 10-10-0049-46
  Que hacer: convertirlos a nulo real antes de contar faltantes.

PROBLEMA 8 - COSAS MENORES
  - NIVEL es constante en los 22 archivos (unico valor "DIVERSIFICADO").
    No sirve para diferenciar registros. Se puede eliminar.
  - Espacios dobles internos en el grupo B: 11 en ESTABLECIMIENTO, 3 en
    DIRECCION. El grupo A tiene 0.
    Ejemplo: "CENTRO EDUCATIVO  EL PROGRESO 5A."
  - Contaminacion entre ESTABLECIMIENTO y DIRECCION en el grupo B: pedazos de
    direccion pegados al nombre y nombres de persona pegados a la direccion.
    Ejemplo real (CODIGO 16-01-0137-46):
      ESTABLECIMIENTO = "INSTITUTO MIXTO NOCTURNO FRANCISCO MARROQUIN 6A."
      DIRECCION       = "AVENIDA 1-15 ZONA 4 JORGE EDUARDO PAQUE LAZARO"
    El "6A." va con la direccion y el nombre de persona no deberia estar ahi.
  - PLAN del grupo A tiene el dominio fragmentado: SEMIPRESENCIAL,
    SEMIPRESENCIAL (FIN DE SEMANA), SEMIPRESENCIAL (UN DIA A LA SEMANA) y
    SEMIPRESENCIAL (DOS DIAS A LA SEMANA) son 4 categorias separadas.
  - DEPARTAMENTAL no tiene relacion 1 a 1 con DEPARTAMENTO en ningun grupo:
    en A, QUICHE se parte en QUICHE (261) y QUICHE NORTE (61).
    en B, GUATEMALA se parte en NORTE, SUR, ORIENTE y OCCIDENTE.
    Esto NO es un error, son jurisdicciones administrativas reales.


C. VALORES FALTANTES POR VARIABLE

GRUPO A (de 4033 registros):
  Variable          Faltantes   %
  (sin nombre)      4033        100.00   <- columna vacia, borrar
  DIRECTOR          475         11.78
  TELEFONO          295         7.31
  SUPERVISOR        118         2.93
  DISTRITO          115         2.85
  DIRECCION         39          0.97
  ESTABLECIMIENTO   1           0.02     <- CODIGO 11-05-1304-46
  Las otras 11 variables: 0 faltantes.

GRUPO B (de 5673 registros):
  Variable             Faltantes   %
  PLAN                 817         14.40   <- recuperable, problema 1
  JORNADA              638         11.25   <- recuperable, problema 1
  DIRECCION            600         10.58
  SUPERVISOR_DIRECTOR  449         7.91
  TELEFONO             394         6.95
  DISTRITO             199         3.51
  ESTABLECIMIENTO      109         1.92
  STATUS               55          0.97    <- recuperable, problema 1
  MODALIDAD            55          0.97    <- recuperable, problema 1
  AREA                 2           0.04    <- CODIGO 16-01-0982-46, 05-02-0065-46
  Las otras 6 variables: 0 faltantes.

  Dato util: de los faltantes del grupo B, 1565 (PLAN + JORNADA + STATUS +
  MODALIDAD) NO son perdida real, son el problema 1. Se recuperan parseando.

  Donde se concentran los faltantes:
    Grupo A: reparto parejo entre departamentos, sin foco.
    Grupo B: GUATEMALA es el que mas aporta (es el archivo mas grande, 1908
      registros). HUEHUETENANGO destaca por sus 242 direcciones vacias, de
      600 en total.


D. DOMINIOS DE LAS VARIABLES CATEGORICAS

Comparar las dos columnas es la forma rapida de ver el efecto del problema 1:
las categorias que "faltan" en B no desaparecieron, estan dentro de
DEPARTAMENTAL.

  NIVEL          A: DIVERSIFICADO (4033)      B: DIVERSIFICADO (5673)
                 Constante en ambos.

  SECTOR         A: PRIVADO 3165, OFICIAL 633, COOPERATIVA 177, MUNICIPAL 58
                 B: PRIVADO 4712, OFICIAL 725, MUNICIPAL 118, COOPERATIVA 118
                 OK en ambos, mismas 4 categorias.

  AREA           A: URBANA 3042, RURAL 991
                 B: URBANA 4271, RURAL 1400, vacio 2
                 OK en ambos.

  MODALIDAD      A: MONOLINGUE 3817, BILINGUE 216
                 B: MONOLINGUE 5369, BILINGUE 249, vacio 55
                 OK en ambos.

  STATUS         A: ABIERTA 2524, CERRADA TEMPORALMENTE 901,
                    CERRADA DEFINITIVAMENTE 570, TEMPORAL NOMBRAMIENTO 21,
                    TEMPORAL TITULOS 17
                 B: ABIERTA 3514, CERRADA TEMPORALMENTE 1389,
                    CERRADA DEFINITIVAMENTE 715, vacio 55
                 B perdio TEMPORAL NOMBRAMIENTO y TEMPORAL TITULOS.
                 Tambien aparece "SIN ESPECIFICAR" dentro de DEPARTAMENTAL,
                 categoria que no existe en A.

  JORNADA        A: VESPERTINA 1403, DOBLE 1338, MATUTINA 778, SIN JORNADA 369,
                    NOCTURNA 119, INTERMEDIA 26
                 B: DOBLE 1871, VESPERTINA 1659, MATUTINA 1295, NOCTURNA 172,
                    INTERMEDIA 38, vacio 638
                 B perdio SIN JORNADA.
                 Tambien aparece "INTERCALADO" dentro de DEPARTAMENTAL,
                 categoria que no existe en A.

  PLAN           A: DIARIO(REGULAR) 2619, FIN DE SEMANA 933,
                    SEMIPRESENCIAL (UN DIA A LA SEMANA) 189,
                    SEMIPRESENCIAL (FIN DE SEMANA) 159, A DISTANCIA 54,
                    VIRTUAL A DISTANCIA 24, SEMIPRESENCIAL 21, DOMINICAL 13,
                    SABATINO 11, SEMIPRESENCIAL (DOS DIAS A LA SEMANA) 7,
                    MIXTO 2, IRREGULAR 1
                 B: DIARIO(REGULAR) 3372, FIN DE SEMANA 1460, SABATINO 18,
                    DOMINICAL 5, MIXTO 1, vacio 817
                 B perdio SEMIPRESENCIAL y sus 3 variantes, A DISTANCIA,
                 VIRTUAL A DISTANCIA e IRREGULAR.

  DEPARTAMENTO   A: 11 valores, sin tildes.
                 B: 11 valores, sin tildes.
                 OK en ambos.

  DEPARTAMENTAL  A: 12 valores. OK salvo QUICHE NORTE (jurisdiccion real).
                 B: 120 valores. ROTO, ver problema 1.


E. LO QUE ESTA BIEN, NO TOCAR

  - 0 registros duplicados exactos en los 22 archivos.
  - 0 codigos repetidos. CODIGO es llave unica: 4033 unicos en A, 5673 en B.
  - 0 solapamiento de CODIGO entre grupos: los 22 departamentos no se traslapan.
  - CODIGO cumple el formato NN-NN-NNNN-NN en el 100% de los 9706 registros.
  - 0 espacios sobrantes al inicio o final de los campos de texto.
  - SECTOR y DEPARTAMENTO: sin faltantes y con dominios limpios en los 2 grupos.
  - AREA, STATUS, MODALIDAD, JORNADA y PLAN: sin faltantes en el grupo A.


F. CIFRAS GLOBALES

  Archivos                                  22
  Estructuras distintas                     2
  Registros totales                         9706  (4033 en A, 5673 en B)
  Variables                                 18 en A, 16 en B
  Departamentos cubiertos                   22
  Duplicados exactos                        0
  Codigos repetidos                         0
  Registros con columnas corridas           817   (todos en el grupo B)
  Columnas 100% vacias                      1     (la sin nombre, grupo A)
  Variables constantes                      1     (NIVEL, en ambos grupos)
  Telefonos fuera del estandar de 8 digitos 143   (43 en A, 100 en B)
  Faltantes recuperables via problema 1     1565


NOTA FINAL

Los archivos "_limpio" estan mas dañados que los originales. Vale la pena
preguntar de donde salieron y si existe la version cruda de esos 11
departamentos: recuperarlos desde la fuente es mas barato que parsear las
817 cadenas y ademas resolveria el problema 3, que no tiene arreglo
automatico confiable.
