# Gilbert.dice

El origen de la idea, primero del generador y luego de Gilbert, no está donde normalmente la ubico, es anterior.

Hace unos cuantos años estuve saliendo con un hombre que quería aprender a escribir mejor y se me ocurrió crearle un juego con el que podía generar ideas con las que luego trabajar y crear textos; no solo partía con la idea de obligar y gamificar la experiencia de escribir cuentos, sino con la de entrenar la imaginación. Se lo regalé la navidad de 2018.

Poco después creé una copia un poco más simple con la que empezaría el taller de escritura en enero de 2019 y que, básicamente, era una caja llena de recortes de cartulina con adjetivos, verbos y sujetos, además de un dado y otras tarjetitas separadas con retos. Como el taller, por comodidad, lo hacíamos en una cafetería del centro, era un poco engorroso llevar la cajita, así que para febrero ya tenía preparado el juego en una hoja de Excel, con la comodidad añadida de que la idea estaba a un solo clic y no a varias tiradas de dados.

Durante 2019 nos ofreció retos sobre las que escribir un tanto difíciles y que dieron lugar a textos que costaba leer: a veces eran tan absurdos que tenías que esforzarte para no reírte (aunque, a veces, Iván, obligaba a hacer pausas por sus risas contagiosas). El generador me gusta tal como es y funciona perfectamente, pero llegó 2020 y el bootcamp de Ciencia de datos. Donde, por fin, pude superar mi miedo a programar (algún día contaré esta anécdota en donde corresponde).

En ese momento me dije: podría plantear el Generador de ideas con Python, al final sería más cómodo y podría acabar con un programita curioso al que ir implementándole cositas y funcionalidades… etc. Me gustó la idea y, a ratos, pensaba en cómo plantear y desarrollarlo, cómo tendría que transformar las columnas con las palabras para que interactuaran y, además, que esta vez no te arrojara las palabras sueltas (como hacía el Excel), sino una frase.

Me senté delante del ordenador, abrí un cuaderno de Jupyter y me puse a trastear.

¿Por qué Gilbert? El nombre viene de un personaje de una recopilación muy esquizoide que tengo pendiente publicar. En el caso de este proyecto, será un generador de frases del tipo Un pájaro azul debe cantar y cuyo objetivo es generar ideas aleatorias que se conviertan en detonantes de historias. Algo sencillo.

## Un poco de contexto
*(04 de febrero de 2020)*

En 2019 comencé un taller con amigos para el que ideé una caja llena de tarjetas con muchas palabras diferentes que se dividían en tres grupos: sustantivos, adjetivos y verbos. La idea inicialmente era sacar de cada grupo una palabra y formar con ella la frase correspondiente de sujeto + adjetivo debe verbo. Esa frase te decía de forma muy libre e interpretable lo que debía hacer ese sujeto con una cualidad para finalizar el relato.

Como cargar con la caja era un poco engorroso, me planteé crear una versión en algún programa con el que fuera fácil hacerlo y recordé algunas características de Excel que me permitían crear lo que buscaba. Esta versión la podéis descargar en el enlace que tenéis a continuación; aunque mi idea es rehacerlo con un enfoque más complejo y limpio.

Una futura propuesta de versión con Python y un json, o esa es la intención por el momento; igual cuando comience a hacerlo se me ocurre alguna otra forma de hacerlo.

Todavía, como todo lo que está en esta página, está a la espera de que saque un poco de tiempo entre el trabajo y el Bootcamp de Ciencia de Datos. Tampoco quiero precipitarme; si lo hiciera ahora, probablemente, habría cosas que haría patosamente diferentes a cuando termine con la formación; así que, por ahora, voy haciendo pruebas, dándole forma y demás, pero nada que pueda mostrarse (qué le voy a hacer, no me gusta enseñar las cosas a medias).

Si te has descargado el Excel, verás que solo te suelta palabras. Para la futura versión quiero que el resultado dé directamente la frase hecha, concordando tanto el género de los sujetos con los artículos que lo acompañan y el adjetivo. Tengo una idea muy estructurada de cómo podría hacerlo, ahora solo me falta solventar un par de flequillos para poder comenzar a escribir el código.

## El origen del nombre
*(16 de enero de 2021)*
¿Por qué se llama Gilbert?, es una de las preguntas que alguna vez los amigos me han hecho cuando les he enseñado el programita que estoy haciendo y, la verdad, explicarlo, puede ser un poco complejo ya que las referencias se remontan a un blog que mantuve durante la carrera, hace ya más de 10 años.

Cuando me vine a Madrid, inauguré un blog con unas amigas, que actualmente mantiene a modo personal una de ellas, llamado Cosas del domingo; este blog surgió por culpa de un relato escrito en segunda persona en aquella época y en el que cada una aportaba su granito de arena.

Se puede encontrar una versión de Cosas del domingo en mi web, que es una remodelación posterior en la que solo están las partes que escribí. Después de terminar el proyecto de Cosas del domingo, inauguré en solitario un blog (cerrado hace años), llamado Diente de dragón; pero, por suerte, mantengo mi propia hemeroteca y hago copias de seguridad desde que tengo 18 años (no me ha hecho falta perder información importante para entender la importancia de realizar copias regularmente).

En Diente de dragón, publicaba una serie de relatos cortos llamados retazos que lo único que tenían en común es que utilizaban personajes anónimos: nunca les ponía nombre ni los identificaba. Era el encanto particular que tenían (para mí, claro). Hace unos cuantos años me dediqué a recopilar y organizar (como buena gestora de información) todos aquellos relatos que tenía desperdigados y guardados en diferentes formatos y lugares; tratando, siempre que fuese posible, de datarlos. Los que habían sido publicados en el blog eran relativamente fáciles, en otros la labor fue más compleja.

Cuando llegué a la colección de retazos de Diente de dragón, se me ocurrieron varias formas de trabajar esos textos; entre ellos, crear una antología de relatos con una revisión y selección de los que, diez años después, juzgase que podían merecer la pena. El problema de ser textos propios es que ves cómo puedes mejorarlos cada vez que los lees y es una tarea en la que todavía me sumerjo a ratos. Creé la antología de Diente de dragón, que todavía tengo en proceso de corrección y maquetación y, como hilo conductor creé a un personaje que justificara el conjunto: Gilbert. Diente de dragón es el diario que este personaje desarrolla durante su estancia en un psiquiátrico.

Existe un spin-off de esta antología, Dientes de león, que ya tengo publicada en Lektu, que se compone de microrrelatos y que es creación de un personaje que Gilbert se inventa para Dientes de dragón; porque sí, me gusta enredar las cosas.

Cuando me planteé pasar a un programa el generador de ideas que creé para el taller de Escríbeme, Cerveza, sentí que debía darle un nombre más “atractivo”; recordé entonces a Gilbert ya que, el generador que hice en Excel y, por supuesto, su versión en Python, daban ideas tan inconexas, extrañas y extravagantes que bien podrían haber sido parte de la antología de relatos de Gilbert. Podría decirse que fue una asociación natural.

En cuanto al .dice() es, claramente, culpa del Simon dice y de las clases de Python.

## El origen de la idea
*(23 de enero de 2021)*

El origen de la idea, primero del generador y luego de Gilbert, no está donde normalmente la ubico, es anterior.

Hace unos cuantos años estuve saliendo con un hombre que quería aprender a escribir mejor y se me ocurrió crearle un juego con el que podía generar ideas con las que luego trabajar y crear textos; no solo partía con la idea de obligar y gamificar la experiencia de escribir cuentos, sino con la de entrenar la imaginación. Se lo regalé la navidad de 2018.

Poco después creé una copia un poco más simple con la que empezaría el taller de escritura en enero de 2019 y que, básicamente, era una caja llena de recortes de cartulina con adjetivos, verbos y sujetos, además de un dado y otras tarjetitas separadas con retos. Como el taller, por comodidad, lo hacíamos en una cafetería del centro, era un poco engorroso llevar la cajita, así que para febrero ya tenía preparado el juego en una hoja de Excel, con la comodidad añadida de que la idea estaba a un solo clic y no a varias tiradas de dados.

Durante 2019 nos ofreció retos sobre las que escribir un tanto difíciles y que dieron lugar a textos que costaba leer: a veces eran tan absurdos que tenías que esforzarte para no reírte (aunque, a veces, Iván, obligaba a hacer pausas por sus risas contagiosas). El generador me gusta tal como es y funciona perfectamente, pero llegó 2020 y el bootcamp de Ciencia de datos. Donde, por fin, pude superar mi miedo a programar (algún día contaré esta anécdota en donde corresponde).

![image1.png](https://github.com/Erebyel/Erebyel/blob/main/proyectos-personales/Gilbert.dice/image1.png)

En ese momento me dije: podría plantear el Generador de ideas con Python, al final sería más cómodo y podría acabar con un programita curioso al que ir implementándole cositas y funcionalidades… etc. Me gustó la idea y, a ratos, pensaba en cómo plantear y desarrollarlo, cómo tendría que transformar las columnas con las palabras para que interactuaran y, además, que esta vez no te arrojara las palabras sueltas (como hacía el Excel), sino una frase.

Me senté delante del ordenador, abrí un cuaderno de Jupyter: [Desarrollo inicial de Gilbert](https://github.com/Erebyel/Erebyel/blob/main/proyectos-personales/Gilbert.dice/Gilbert_desarrollo%20inicial%20de%20Gilbert.ipynb) y me puse a trastear.
