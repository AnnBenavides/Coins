# Coins
Administrador de compra y venta restringida para el curso [FM307] Innovación y Tecnologia de EdV
Este sitio ha sido [desplegado en PythonAnywhere](http://annbenavides.pythonanywhere.com) desde Enero 2018 hasta Abril del mismo año

# Version 2 (Verano 2018)
## Requerimientos
- Python version 3.4
- Virtualenv, elementos integrados en _env_
  - Django 1.8
  - Bootstrap

## Instalar Python
### En Windows
Puedes descargar desde el [sitio de Python](https://www.python.org/downloads/) una versión superior a 3.4.3 e instalar el archivo .msi. Es importante recordar la ruta en donde se ha insalado Python.

En la segunsa pantalla del asistente, _Customize_, ve hasta abajo y elige la opción _"Add python.exe to the Path"_ .

### En Linux
Desde la terminal:
```sh
~$ sudo apt-get install python3.4
```

## Instalar Git
### En Windows
Puedes descargar desde el [sitio de Git](http://gitforwindows.org) e instalar el archivo .exe. Puedes hacer clic en "Next" para todos los pasos excepto en uno; en el quinto paso titulado "Adjusting your PATH environment", elije "Run Git and associated Unix tools from the Windows command-line" (la última opción). Aparte de eso, los valores por defecto funcionarán bien. "Checkout Windows-style, commit Unix-style line endings" también está bien.

### En Linux
Puedes descargar e instalar Git desde [el sitio de Git](http://git-scm.com/download/linux) o desde la terminal usa:
```sh
# instalar git con dnf
$ sudo dnf install git-all

# instalar git con apt-get
$ sudo apt-get install git-all
```

## Como inicializar
### En Windows
```sh
#copiar repositorio
~\> git clone https://github.com/AnnBenavides/Coins.git
~\> cd Coins
~\Coins> cd v.2.0

#iniciar el entorno virtual
~\Coins\v.2.0 > env\Scripts\activate
(env) ~\v.2.0>

# ficheros estáticos
(env) ~/v.2.0 $ python manage.py collectstatic
You have requested to collect static files at the destination
location as specified in your settings:
    /home/annbenavides/Coins/v.2.0/static
This will overwrite existing files!
Are you sure you want to do this?
Type 'yes' to continue, or 'no' to cancel: yes

#cargar el modelo
(env) ~\v.2.0> python manage.py makemigrations app
(env) ~\v.2.0> python manage.py migrate

#configurar administrador
(env) ~\v.2.0> python manage.py createsuperuser
Username:
Email address:
Password:
Password (again)
Superuser created succesfully

#correr el proyecto en la direccion local http://127.0.0.1:8000/
(env) ~\v.2.0> python manage.py runserver
```

### En Linux
```sh
# copiar repositorio
~/ $ git clone https://github.com/AnnBenavides/Coins.git
$ cd Coins/v.2.0/

# iniciar entorno virtual
~/v.2.0 $ source env/bin/activate
(env) ~/v.2.0 $

# instalar django
(env) ~/v.2.0 $ pip instal django==1.8 whitenoise

# ficheros estáticos
(env) ~/v.2.0 $ python manage.py collectstatic
You have requested to collect static files at the destination
location as specified in your settings:
    /home/annbenavides/Coins/v.2.0/static
This will overwrite existing files!
Are you sure you want to do this?
Type 'yes' to continue, or 'no' to cancel: yes

# cargar modelo
(env) ~/v.2.0 $ python manage.py makemigrations app
(env) ~/v.2.0 $ python manage.py migrate

#correr el proyecto en la direccion local http://127.0.0.1:8000/
(env) ~\v.2.0> python manage.py runserver
```
