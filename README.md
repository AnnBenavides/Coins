# Coins
Administrador de compra y venta restringida para el curso [FM307] Innovación y Tecnologia de EdV

# Version 2 (Verano 2018)
## Requerimientos
- Python version 3.4
- Virtualenv, elementos integrados en _env_
  - Django 1.8
  - Bootstrap

## Como inicializar
### En Windows
```sh
#iniciar el entorno virtual
~Coins\> env\Scripts\activate
(env) ~\Coins>

#cargar el modelo
(env) ~\Coins> python manage.py makemigrations app
(env) ~\Coins> python manage.py migrate

#configurar administrador
(env) ~\Coins> python manage.py createsuperuser
Username:
Email address:
Password:
Password (again)
Superuser created succesfully

#correr el proyecto en la direccion local http://127.0.0.1:8000/
(env) ~\Coins> python manage.py runserver
```

