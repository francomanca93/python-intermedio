<div align="center">
    <h1>Curso de Python Intermedio</h1>
    <img src="https://imgur.com/7r7WRNl.png" width="">
</div>

## Tabla de contenidos

- [Introducción](#introducción)
  - [El Zen de Python](#el-zen-de-python)
  - [¿Qué es la documentación?](#qué-es-la-documentación)
- [Entorno virtual](#entorno-virtual)
  - [¿Qué es un entorno virtual?](#qué-es-un-entorno-virtual)
  - [Creación de un entorno virtual](#creación-de-un-entorno-virtual)
  - [Instalación de dependencias con pip](#instalación-de-dependencias-con-pip)
  - [Una alternativa: Anaconda](#una-alternativa-anaconda)
- [Alternativa a los ciclos: comprehensions](#alternativa-a-los-ciclos-comprehensions)
  - [Listas y diccionarios anidados](#listas-y-diccionarios-anidados)
  - [List comprehension](#list-comprehension)
  - [Dictionary comprehensions](#dictionary-comprehensions)
- [Conceptos avanzados de funciones](#conceptos-avanzados-de-funciones)
- [Manejo de errores](#manejo-de-errores)
- [Manejo de archivos](#manejo-de-archivos)

# Introducción

## El Zen de Python

[El Zen de Python](https://www.python.org/dev/peps/pep-0020/) se compone por los principios para escribir tu código de manera clara, sencilla y precisa. Estos son:

- **Bello es mejor que feo**:
  - Pyhton es estéticamente superior a cualquier otro lenguaje de programación. Al momento de escribir código, es mejor que sea de manera limpia y estética.
- **Explícito es mejor que implícito**:
  - Hacer más fácil que las otras personas entiendan el código.
- **Simple es mejor que complejo**:
  - Es mejor tener una implementación simple, que ocupe pocas lineas de código y sea entendible, a que sea una larga y complicada.
- **Complejo es mejor que complicado**:
  - Si tenemos que extendernos en la implementación y hacerla más compleja para que el código si se entienda, esto es mejor que hacerlo simple y mal.
- **Plano es mejor que anidado**:
  - El anidamiento es cuando tenemos un bloque de código dentro de otro bloque de código (dependiendo de este). Esto se nota en Python por la identación, nos quedarían estos bloques muy corridos a la derecha.
  - Es mejor evitar el anidamiento, y hacer las cosas de manera plana.
- **Espaciado es mejor que denso**:
  - Por la identación de Python (sus sangrías), este principio se nos hace imposible de esquivar. El código inevitablemente es espaciado.
- **La legibilidad es importante**:
  - Es importante que otros programadores puedan entender lo que estamos escribiendo. Esto hace más fáciles las cosas cuando trabajemos con otros en los proyectos.
- **Los casos especiales no son lo suficientemente especiales como para romper las reglas (sin embargo, la practicidad le gana a la pureza)**:
  - Siempre que podamos respetar estas reglas que nos plantea Python, es mejor así. Sin embargo, si por el hecho de hacer un código muy puro o muy ‘Pythonista’, este pierde legibilidad, es mejor ser más prácticos y romper o saltearnos algunas de estas reglas para que el código sea más eficiente. Por lo tanto, llegado el momento debermos decidir si es mejor hacer las cosas de manera pura o práctica.
- **Los errores nunca deberían pasar silenciosamente (a menos que se silencien explícitamente)**:
  - Manejar los erroes es fundamental. Cada error nos dice algo y hay que prestarle atención. A menos que seas capaz de silenciar un error explícitamente, aunque para esto hay que tener criterio.
- **Frente a la ambiguedad, evitar la tentación de adivinar**:
  - Nuestro código debería solamente tener una interpretación. Si en un contexto significa algo, y en otro otra cosa, es mejor que lo revisemos y busquemos una solución.
- **Debería haber una, y preferiblemente sola, una manera obvia de hacerlo. (A pesar de que esa manera no sea obvia a menos que seas holandés)**:
  - Esto hace referencia al creador de Python ''Guido van Rossum", que de manera muy inteligente encontrar las soluciones precisas a los problemas, y deberíamos imitarlo.
- **Ahora es mejor que nunca**:
  - Es mejor desarrollar nuestra solución cuánto antes, no dejarlo para mañana o para mas adelante.
- **A pesar de que nunca es muchas veces mejor que ahora mismo**:
  - Si por hacer las cosas ya y tenemos poco tiempo, si es mejor dejarlo para después y no hacerlo apurado y mal.
- **Si la implementación es díficil de explicar, es una mala idea, y si es fácil de explicar, puede que sea una buena idea**:
  - Si somos capaces de explicar nuestra implementación a otros desarrolladores paso a paso, es una buena idea. En cambio si no podemos hacerlo, significa que ni nosotros entendemos la implementación y deberíamos repensar nuestra forma de encarar la solución.
- **Los espacios de nombres son una gran idea, ¡Tengamos más de esos! (namespaces)**:
  - Es el nombre que se ha indicado luego de la palabra import, es decir la ruta (namespace) del módulo.

## ¿Qué es la documentación?

> La documentación es la biblia de cualquier programador

La documentación es fundamental para aprender cualquier lenguaje de programación, ya que nos ayuda a entender todas esas pequeñas piezas para que todo funcione correctamente.

La documentación de python esta en: https://docs.python.org/es/3/

PEP (propuestas de mejoras de python)

En el apartado [PEPindex](https://www.python.org/dev/peps/) Nos indica como el lenguaje funciona y como se debería escribir de forma correcta. Todo lo relacionado a buenas practicas en la escritura del código (identacion, comentarios, nombres recomendados) lo encontramos en [PEP8](https://www.python.org/dev/peps/pep-0008/).

# Entorno virtual

## ¿Qué es un entorno virtual?

> El entorno virtual permite aislar las dependencias de los proyectos en Python.

Los entornos virtuales son de mucha utilidad ya que nos ayudan a tener versiones especificas de librerías o módulos a un proyecto sin afectar a otros. De esta forma en el mismo equipo pueden coexistir distintos proyectos con distintas versiones de la misma librería o modulo.

- **Sin entorno virtual**

Tenemos a nuestros modulos de forma global.
![](https://imgur.com/FwmWrnP.png)

Si un modulo se actualiza puede afectar a un proyecto
![](https://imgur.com/8LWuztH.png)

- **Con entorno virtual**

Tenemos a nuestros modulos por proyecto
![](https://imgur.com/6rRaiMe.png)

Si un modulo se actualiza solo afectará al proyecto que tenga ese entorno.
![](https://imgur.com/RMz5eCI.png)

## Creación de un entorno virtual

Python 3 trae la creación y manejo de entornos virtuales como parte del modulo central.

Para crear un entorno virtual utilizas:

`python3 -m venv .NOMBRE-ENTORNO`

Nota:.NOMBRE-ENTORNO es el nombre de del ambiente. El punto delante es para que sea una carpeta oculta

Para activarlo:

`source -m ./.env/bin/activate`

Si queremos desactivarlo:

`deactivate`

Si deseamos ver las librerías instaladas en el ambiente:

`pip freeze`

## Instalación de dependencias con pip

En Python `pip` es como el `npm` de JavaScript, y el archivo `requeriments.txt` es como el `package.json` de JavaScript.

Pip (package installer for python) Nos permite descargar paquetes de terceros para utilizarlos en nuestro environment, ademas se puede definir una versión especifica del paquete.

- `pip install <paquete>` instala el paquete(pandas , matplotlib, bokeh, etc) que se especifique.
- `pip freeze` muestra todos los paquetes instalados en tu ambiente virtual

Es importante recordar que esto se debe correr con el entorno virtual activado (avenv), de esta manera todas las dependencias que instalemos se guardaran para este entorno virtual (de lo contrario se guardarían de manera global, que es justo lo que no queremos).

Algo importante, si estás manejando git, es bueno siempre ignorar la carpeta venv, esto porque realmente no nos importa subir todo eso al repositorio. Cualquier otro programador que trabaje con nuestro código creará su propio entorno virtual e instalará las dependencias que dejamos en nuestro `requeriments.txt`.

Si quisiéramos que alguien mas pueda ejecutar nuestro proyecto es importante compartir que librería y versión hemos empleado; eso se realiza con el comando:

- `pip freeze > requirements.txt`

El resultado de `pip freeze` se escribe en `requirements.txt` (puedes usar otro nombre pero el mostrado es una buena practica)

Para instalar paquetes desde un archivo como requirements.txt ejecutamos:

- `pip install -r requirements.txt`

## Una alternativa: Anaconda

[Anaconda](https://www.anaconda.com/products/individual)

![](https://imgur.com/xwX9Ftl.png)

Podemos crear un entorno virtual de anaconda mediante el Anaconda Prompt con los siguientes comandos.

- Crear entorno virtual
`conda create --name venv`

- Para activar el entorno virtual se utiliza:
`conda activate venv`

- Para desactivarlo
`conda deactivate`

- Para ver los entornos virtuales instalados se usa
`conda env list`

- Instalar modulos
`conda install <modulo>`

- O también mediante un archivo requirements.txt
`conda install --file requirements.txt`

- Para crear el archivo requirements.txt parecido al freeze en python se usa
`conda list --export > requirements.txt`

# Alternativa a los ciclos: comprehensions

## Listas y diccionarios anidados

[Practica de Listas y diccionarios anidados](lists_and_dicts.py)

## List comprehension

[Practica de Listas comprehension](list_comprehension.py)

[List comprehension - Doc oficial](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

Como se lee lo siguiente:

Para cada elemento en el iterable, ese elemento, solo si se cumple la condición.

- PARTE 2: Para cada elemento en el iterable,
- PARTE 1: ese elemento,
- PARTE 3: solo si se cumple la condición.

![](https://imgur.com/Zs2iH9B.png)

Ejemplo realizado tambien en el script:

Como se lee lo siguiente:

Guardame en una lista:
Cada elemento en que se encuentre en un rango de 1 a 101, que se elemento sea elevado al cuadrado, solo si no son multiplos de 3 (elemento aplicando el modulo 3 sea diferente de 0)

![](https://imgur.com/1lRhTHW.png)

![](https://imgur.com/k2MrsGc.png)

## Dictionary comprehensions

[Practica de Listas comprehension](dict_comprehension.py)

[Dict comprehension - Doc oficial](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

Para cada elemento en un iterable yo voy a colocar una llave y un valor solo si se corresponde a una condicion

![](https://imgur.com/iDTq9Qk.png)

Ejemplo:

![](https://imgur.com/uPJOB0W.png)
# Conceptos avanzados de funciones

# Manejo de errores

# Manejo de archivos
