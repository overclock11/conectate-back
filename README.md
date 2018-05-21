# Conectate

![Codeship Status for sergioperezf/conectate-back](https://app.codeship.com/projects/8af1a200-265e-0136-0fb5-1a4fdef819d4/status?branch=develop)  ![Heroku](https://heroku-badge.herokuapp.com/?app=contectate-test) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/91d8009bdb164b3188f539a3922b6edb)](https://www.codacy.com/app/se.perezf/conectate-back?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sergioperezf/conectate-back&amp;utm_campaign=Badge_Grade)

## Instrucciones de instalación

### Requerimientos

- npm
- pip
- python 3
- virtualenv

Para instalar el proyecto de manera local, primero hay que instalar el backend.

```
cd conectate-back
virtualenv . -p python3
source bin/activate
pip install -r requirements.txt
```

Esto instalará las dependencias de python en la carpeta. 

Después, instalamos las depencendias de Javascript:

```
export FE_BRANCH=develop
npm install
```

Esto instalará el repositorio de front end, sus dependencias, y compilará el código.

Ahora, estamos listos para correr el proyecto localmente.

## Ejecutar el proyecto localmente

Primero, tenemos que crear una base de datos de acuerdo con lo especificado en `conectate_back/settings.py`. Estos parámetros se pueden modificar por medio de variables de entorno.

Depués, corremor `python manage.py migrate`, y finalmente, `python manage.py runserver`. Ahora tendremos el servidor de desarrollo funcionando.

## Desarrollo del front end

Para empezar a desarrollar en el front-end, correr el siguiente comando desde el repositorio de back-end:

```
npm run fe-dev
```

Esto iniciará el proceso que escucha archivos modificados de Angular, y compila el fuente de front end al directorio correcto automáticamente.

## Despliegue en Heroku

Para el despliegue en Heroku, es necesario contar con un Dyno que esté configurado para dos buildpacks:

- `heroku/python`
- `heroku/nodejs`

Esto se puede configurar en `apps/<app>/settings`. Igualmente, al crear el Dyno, se debe asignar el add-on Heroku Postgress, y se deben llenar las variables de configuración encontradas en `conectate_back/settings.py` de acuerdo a la configuración del add-on. Además de esto, se debe añadir la variable `FE_BRANCH` con el branch del repositorio de front end que se quiera desplegar.

Con estas configuraciones, ya se puede desplegar en Heroku el repositorio `conectate-back` por medio de `git`, como se expone en la documentación encontrada en https://dashboard.heroku.com/apps/app/deploy/heroku-git