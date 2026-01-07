# ÍNDICE
<ul>
<li><a href='#introduccion'>Introducción</a></li>
<li><a href='#manual'>Manual</a></li>
<li><a href='#metodologia'>Metodología</a></li>
<li><a href='#descripcion'>Descripción técnica</a></li>
<li><a href='#diseño'>Diseño</a></li>
<li><a href='#implementacion'>Implementación</a></li>
<li><a href='pruebas'>Pruebas</a></li>
<li><a href='#tiempo'>Estudio de tiempo invertido</a></li>
<li><a href='#ia'>Uso de la IA</a></li>
<li><a href='#conclusion'>Conclusión</a></li>
</ul><hr/><hr/>

## <div id= 'introduccion'>Introducción</div>

Juan Mateo Álvarez Álvarez  - <a href='https://github.com/Juan071825'>@Juan071825</a> <br/>
Adrián González González    - <a href= 'https://github.com/Adriceka'>@Adriceka</a>

Este proyecto consiste en recrear en el lenguaje de programación python el juego de mesa Mastermind. Además de python también hemos utilizado otras herramientas y lenguajes como git, markdown, ruff.

## <div id='manual'>Manual</div>

## <div id= 'metodologia'>Metodología</div>

Para llevar a cabo este proyecto decidimos empezar por la lógica del proyecto.
Para saber que módulos de python con la lógica del programa teníamos que crear, seguimos la guía del algoritmo genético del libro Artificial Intelligence Algorithms de Rishal Hurbans.

La metodología empleada tiene su enfoque inspirado en <a href='https://es.wikipedia.org/wiki/Desarrollo_guiado_por_pruebas'>TDD</a> y consta de tres pasos:

<ol>
<li> Entre los dos integrantes del grupo hacemos una lista de requisitos que debe cumplir un módulo, de funcionalidades que debe de tener. Esto nos sirve para el siguiente paso. </li><br/>

<li> Uno se dedica a desarrollar el módulo utilizando, en un primer momento, las salidas por consola de guía, mientras que el otro creará los casos test.</li> <br/>

<li> La última fase es la de comprobación, en la que se verá si un módulo pasa los casos test creados para él.</li><br/>
</ol>

Para la documentación simplemente seguimos los ejemplos dados en clase como guía de conteniudos que debía tener nuestro <a href='https://es.wikipedia.org/wiki/README'>README</a>.

## <div id= 'descripcion'>Descripción técnica</div>

### Not list

### Historias de usuario

HISTORIAS USUARIO PROYECTTO MASTERMIND
==================================
## REGLAS DEL JUEGO

1. Ingreso del código secreto

    El usuario introduce una combinación de 4 colores de entre 6 (amarillo, verde, azul, negro, marrón, morado) colores disponibles con posibilidad de repetir, para que el algoritmo tenga un código válido que intentar adivinar.



2. Verificación del código introducido

    Antes de empezar a resolver, el programa revisa que el código secreto tenga 4 colores y que todos pertenezcan al conjunto permitido. Si algo no es correcto, se informa al jugador para que este lo corriga.


3. Inicio del algoritmo 

    El algoritmo comience a generar intentos automáticamente, para ver cómo el algoritmo trata de adivinar mi código. El  algoritmo tendrá un máximo de 14 intentos para resolver mi código, esto según las reglas del Matermind pedido.


4. Generación de cada intento

    En cada ronda, el algoritmo propone una combinación de 4 colores para el acierto del código secreto. Cada nuevo intento debe tener en cuenta la información obtenida en los intentos anteriores e irse acercando más al código oculto.


5. Corrección del intento

  Después de generar una combonación, el programa compara ese intento con el código secreto y se usará para dar pistas as clavijas usando estas instrucciones:

  - Key peg roja: el color es correcto y está en la posición adecuada.
  - Key peg blanco: el color aparece en el código, pero en una posición diferente.
  - Sin key peg: ese color no forma parte del código secreto.



6. Ajuste de posibilidades

    Tras recibir la corrección, el algoritmo debe descartar todas las combinaciones que no son compatibles con la información revelada. A partir de este filtrado, el algoritmo construye un nuevo intento más preciso.


7. Finalización del juego

    El algoritmo continúa este proceso hasta llegar el último intento (el 14) donde puede ocurrir dos soluciones:

    - El algoritmo acierta completamente el código.
    - El algoritmo hace los 14 intentos permitidos sin encontrar la combinación correcta.

    En ambas soluciones, el programa debe mostrar el resultado final del proceso


8. Puntuación del juego

  Al finalizar la partida, el juego debe calcular la puntuación según el número de intentos que el algoritmo ha necesitado para descifrar el código. Según las reglas del Mastermind, el creador     del código gana tantos puntos como filas haya tenido que usar el oponente antes de acertar.







### Arquitectura de la aplicación


## <div id= 'diseño'>Diseño</div>

### Diagrama de componentes

## <div id= 'implementacion'>Implementación</div>

### Tecnologías y herramientas utilizadas

<ul>
<li><a href='https://pypi.org/project/pytest/'>pytest</a>, es un framework de python para testear código.</li>
<li><a href='https://pypi.org/project/pytest-sugar/'>pytest-sugar</a>, es implementa dentro de pytest para hacerlo más visual y amigable.</li>
<li><a heref='https://coverage.readthedocs.io/en/7.13.0/'>Coverage</a>, es una herramienta que vine cuanto porcentaje de tu código se ejecuta al realizarse los casos test.</li>
<li><a href='https://es.wikipedia.org/wiki/Markdown'>Markdown</a>, es un lenguaje de marcado ligero.</li>
<li><a href='https://es.wikipedia.org/wiki/Git'>git</a>, es un software ideado para el control de versiones.</li>
<li><a href='https://docs.astral.sh/ruff/'>ruff</a>, es un <a href='https://keepcoding.io/blog/que-es-un-linter-en-programacion/'>linter</a> y formateador de código python</li>
</ul>

### Backend

### Fronted

<hr/><hr/>

## <div id= 'pruebas'>Pruebas</div>

### Coverage

### Test de unidad

### Test de integridad

## <div id= 'tiempo'>Análisis del tiempo invertido</div>

### Reflexión sobre el tiempo invertido

## <div id= 'ia'>Uso de la IA</div>

## <div id= 'conclusion'>Conclusión</div>

### Cosas a mejorar

### Dificultades




