# RecipesBlog
Blog de recetas de cocina desarrollado por Karen Schurmann, como proyecto final para Coderhouse.

Para la creacion de esta pagina web, se utilizo el framework de python-Django junto con algunas herramientas de html, css y javascript.
Ademas, se utilizaron plantillas html que se descargaron de la pagina "w3schools", "bootstrap" y se modificaron para adaptarlas a las necesidades de la web.

Asimismo, para realizar pruebas, se puede usar el usuario 'admin' cuya contraseña es igual al usuario para entrar al panel de administracion de django y crear o modificar objetos en la base de datos.

Funcionamiento:

Al ejecutar el comando manage.py runserver se inicia el servidor en el localhost de la pc, en el puerto 8000 por defecto.
Una vez que el servidor esta corriendo, la pagina nos redigira a la URL '/' que es el inicio, en donde se puede observar la pagina de inicio de la web.

Para movernos entre las diferentes vistas de la pagina, se puede usar la barra de navegacion situada en la parte superior de la web, teniendo en cuenta que para muchas de las vistas hace falta estar logueado.

De ser necesario, se puede crear un nuevo usuario desde la opcion en la barra de navegacion llamada "register" que solo sera visible si no se esta logueado.

La pagina en si esta compuesta de tres aplicaciones:

En la app de "blog" se pueden ver, crear y editar posteos para el blog. Para ver los posteos solo hace falta dirigirse a la opcion "recetas" en la barra de navegacion. Para editar un posteo, es necesario ser el creador de este y si esto sucede, en la parte inferior del posteo se vera la opcion de editar el posteo. Por ultimo, para crear un nuevo posteo, solo hace falta dirigirse a la URL /blog/add_post.

En la app de "usuarios" se configura todo lo relativo a los usuarios. Para ver el perfil de un usuario solo hace falta hacer click "mi perfil" en la barra de navegacion. Una vez hecho el paso anterior, se puede observar informacion acerca de el usuario y al final de la pagina dos botones: Uno para editar lo referido al perfil y el otro para editar lo referido al usuario (nombre de usuario, mail y contraseña).

En la app de "mensajeria" se pueden enviar y recibir mensajes como un cliente de correo habitual. Solo hace falta dirigirse al apartado de mensajes desde la barra de navegacion y hacer click para dirigirnos a la bandeja de mensajes. Desde este punto se pueden leer mensajes enviados o recibidos e incluso redactar un nuevo mensaje. Hay que tener en cuenta que al redactar un nuevo mensaje, se necesita introducir un nombre de usuario valido para que el mismo sea enviado.



admin: karencoderhouse
password: blogrecetas
