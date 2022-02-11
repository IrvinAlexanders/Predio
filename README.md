# Predio
Sistema de registro de predios creado con Python, Django y Bootstrap.
Primero creé el entorno virtual utilizando el comando python -m venv env
Luego instalé los paquetes necesarios, los cuales estan en el archivo requeriments.txt
Inicié creando el proyecto con el comando de Django (django-admin startproject Predios).
Luego fuí al archivo settings.py y realicé todas las configuraciones necesarias (Añadí las
apps que mas adelante iba a crear, configuré la ruta de los templates, utilicé sqlite3 por
no tener mucho tiempo).
Con el comando de django para crear las apps(django-admin startapp) creé las apps necesarias
para el proyecto, dentro de ellas coloqué las carpetas de templates con sus respectivos codigos
HTML, configuré las rutas de las urls, realicé las pruebas de las apps con la herramienta Insomnia
y todo marchó bien. Para el front creé la carpeta /static donde utilicé bootstrap 4 y algo de 
JavaScrpt básico.

Para que el proyecto funcione hacemos lo siguiente:

git clone https://github.com/IrvinAlexanders/Predio.git en su carpeta destino.
instalamos los paquetes requeridos: python -r requeriments.txt
luego de clonar e instalar los paquetes creamos las migraciones: python manage.py makemigrations
seguido de crear las migraciones, las aplicamos asi: python manage.py migrate
Por ultimo corremos nuestro proyecto: python manage.py runserver
Abrimos nuestro navegador y escribimos: localhost:8000.
