# DracoDB

Llevo unos cuantos años diagramando una base de datos relacional para llevar la producción de una editorial, de forma que la información de los procesos que se llevan a cabo en una, esté disponible en un único lugar. Actualmente, podría decir que estoy en fase de pulir el SQL en su 3ª versión.

Mi intención con este proyecto es terminar un archivo SQL que genere la base de datos ejecutándola a través de un programa tipo SQLiteStudio y que tengas de primeras tanto las tablas como sus relaciones pertinentes y una indexación. Tras esta primera fase, quiero implementar una GUI sencilla a través de Python (con la librería, en principio, tkinter) y ver hasta dónde puedo llegar generando las consultas necesarias para que se implemente la base de datos con la librería sqlite3.

Según vaya desarrollando el proceso de Draco 3, iré actualizando y colocando el código e información que genere en mi web.

Vale, podría irme a algo más complejo, a hacerla con django y tenerla en la web; pero mi intención es que sea una aplicación de escritorio porque meterme en temas de cifrado, de protección de datos y usuarios... me quitaría mucho más tiempo para el resto de mi vida; y no tengo ganas de que nadie me meta en un recurso legal por no haberle puesto encriptadores a la base de datos y esas cosillas. Pero bueno, eso es adelantarme un poco, a ver hasta dónde soy capaz de llegar en el desarrollo.

## Un poco de contexto

La historia de esta base de datos comienza allá por 2014, cuando entro a trabajar en una empresa de servicios editoriales (o, como se empeña en llamarse, editorial de coedición o autopublicación). Cuando me uno al equipo, (en B) para encargarme de toda la gestión de la producción de esa pequeña editorial, descubro que no tiene ningún tipo de control sobre los datos ni la información que genera y necesita para funcionar.

Siempre me ha resultado un misterio cómo ha conseguido sobrevivir, pero tras el impacto inicial de no encontrar absolutamente nada, no saber qué proyectos estaban activos ni en la fase que se encontraban y que la única fuente de la que podía fiarme era el correo electrónico y los mensajes de los autores y colaboradores; decidí que no podía trabajar así.

1. **Draco 1** fue un intento desesperado y muy desestructurado de comenzar a poner orden en aquel caos; su objetivo fue ayudarme a ir tirando los primeros días, agrupando la información y viendo cómo podía procesarse y relacionarse. Desgraciadamente tengo un recuerdo muy vago de ella y no tengo copias de ese primer intento de poner orden a un caos de años.
2. **Draco 2** fue posterior. Por falta de tiempo, también levantada en Access y ya con un diagrama un poco más coherente y, ¡por fin!, que respetaba la integridad referencial. Por cierto, por iniciativa propia y sin recibir ningún tipo de compensación por el trabajo. Aún así, necesitaba trabajar y una base de datos en condiciones era indispensable. Con el uso fui detectando ciertas deficiencias que se quedaron sin arreglar porque, bueno, me despidieron por estar de baja una semana. (A día de hoy me ha dicho un pajarito que sigue siendo una herramienta activa).
3. **Draco 3**. Cuando comencé con el Bootcamp de Ciencia de Datos, unos cuantos años después, me acordé de Draco y recuperé una copia que me hice antes de irme de la editorial (de la bd, no de los datos), pensé en retomar aquel viejo diagrama y rehacerla con una vuelta más y con calma, para subsanar todos los errores y las deficiencias que detecté en su momento en Draco 2; así que, por favor, no tengáis prisa porque quiero hacerla bien.