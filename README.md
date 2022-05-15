# CHALLENGE_SOFKA_CONCURSO_PyR
[![imagen](https://1.bp.blogspot.com/-QoOVw__i6x8/XDYT-K7w0gI/AAAAAAAAONw/iV-KhFuiNB4IBVBYTau4mhCeoDuHXSA7gCLcBGAs/w1200-h630-p-k-no-nu/JEUGOS%2BDE%2BPREGUNTAS.png "imagen")](https://www.google.com/url?sa=i&url=https%3A%2F%2Fpenitenciasyretos.blogspot.com%2F2019%2F01%2Fdisena-tu-propio-juego-de-preguntas-y.html&psig=AOvVaw34ThTBWJGUW7weIVtqWJa8&ust=1652702745137000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCNDQ89W74fcCFQAAAAAdAAAAABAD "imagen")

------------
## Resumen
En este reto vamos a modelar un concurso de preguntas y respuestas, la intención es diseñar una solución que permita tener un banco de preguntas con diferentes opciones para una única respuesta, además cada pregunta debe estar en una categoría o un grupos de preguntas similares del mismo nivel, por cada ronda se deberá asignar un premio a conseguir, las rondas del juego son nivel que van aumentando en la medida que el jugador gana premios.
Dentro del reto se debe considerar lo siguiente:
- Manejo de clases u objetos a nivel de modelamiento.
- Persistencia de datos o guardado de históricos.
-  Manejos de listas o colecciones y ciclos de control adecuados
- Conocimiento de cualquier lenguaje de programación.
- Manejo de Git (versión de control).
## Objetivos
- Realizar un modelamiento de objetos de forma correcta, aplicando los principios de programación orientado a objetos.
- Crear  objetos de entidades; ronda, jugador, categoría, premio,pregunta, opciones, etc...
- Realizar la lógica expuesta para el juego con buenas prácticas de programación, donde se evidencie una estructura y sintaxis coherente.
- Persistencia de los resultados obtenidos de los ganadores del juego.

------------
## Archivos
| Archivo   | Descripcion  |
| ------------ | ------------ |
| controlador.py  | Este archivo contiene el codigo para aceptar las entradas del usuario y delega la representación de datos a una Vista y el manejo de datos a un Modelo. |
|main.py  | Este archivo contiene el codigo para ejecutar el juego.  |
| modelo.py   | Este archivo contiene el codigo para gestionar los datos y define reglas y comportamientos.  |
| operaciones_CRUD.py  | Este archivo contiene el codigo para crear y leer los datos en la base de datos  |
| vista.py  | Este archivo contiene el codigo para presentar los datos al usuario.  |
| base_datos.db  |  Este archivo contiene la base de datos en sqlite3 donde se guardan los datos del juego |
| requirements.txt  | Este archivo contiene los requerimientos para ejecutar el juego  |

------------

## Instrucciones poder jugar
1.  Clone este repositorio en su servidor local
2.  abra la carpeta que en su IDE para el caso de la creacion del juego se uso Visual Studio Code
3. para empezar el juego ejecute el siguiente comando en su terminal ./main.py
4. siga las intrucciones en pantalla para avanzar en el juego recuerde si no esta registrado debe ingresar un numero de registro su nombre y apellido
5. disfrute del juego.

------------

## Modelo Entidad Relacion Base de datos

con el fin de crear una base de datos relacional para el juego se realizo el siguiente modelo Entidad Relacion 
[![Modelo](https://i.ibb.co/fQg52Nv/Screenshot-from-2022-05-15-08-38-31.png "Modelo")](https://ibb.co/N7vPsNS "Modelo")

Se realizo un proceso de normalizacion de cada tabla hasta la tercera forma normal (los campos en negrilla son llaves primarias y fk representa llave foranea) y como resultado se obtuvo el siguiente modelo relacional:
- historico( **idronda(fk),**  **fecha**,** idjugador (fk)**, idpregunta(fk), retiro, idopciones(fk))
- jugadores(**id_jugador,** nombre, apellido)
- preguntas(**id_preguntas**, texto_pregunta,  idcategoria(fk))
- opciones(**id_opciones**, idpregunta(fk), texto_respuesta, veracidad)
- rondaycategoria(**id_ronda**, premio)

## AUTOR

------------

## CARLOS ANDRES PARDO RODRIGUEZ

------------

- [GitHub](https://github.com/ANDRES3021 "GitHub")

- [LinkedIn](https://www.linkedin.com/in/carlos-andres-pardo-rodriguez-8bbb90202/?original_referer=https%3A%2F%2Fgithub.com%2FANDRES3021%2Fholbertonschool-higher_level_programming%2Ftree%2Fmain%2F0x03-python-data_structures "LinkedIn")
- [Twitter](https://twitter.com/CarlosA54648157 "Twitter")

------------