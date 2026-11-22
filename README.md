# Taller Django: programas académicos

Aplicación basada en [DesarrolladorSA11/web1_development](https://github.com/DesarrolladorSA11/web1_development). Registra programas académicos con código único, nombre, estado y facultad.

## Ejecución local

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

Formulario: http://127.0.0.1:8000/programas/crear/  
Administrador: http://127.0.0.1:8000/admin/

Para crear el usuario administrador: `py manage.py createsuperuser`.

## Despliegue en PythonAnywhere

La guía oficial de PythonAnywhere indica subir o clonar el proyecto, instalar sus requisitos en un entorno virtual, crear una aplicación con configuración manual y ajustar el WSGI. En las cuentas con la imagen actual, PythonAnywhere ofrece Python hasta 3.13; el Python 3.14 instalado en Windows no se usa en el servidor.

En una Bash Console de PythonAnywhere:

```bash
git clone https://github.com/kairoblix/Parcial-Final---Django-y-despliegue-en-PythonAnywhere.git
cd Parcial-Final---Django-y-despliegue-en-PythonAnywhere
mkvirtualenv --python=/usr/bin/python3.13 programas-venv
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

En la pestaña **Web**, crea una aplicación Django con **Manual Configuration** y Python 3.13. Configura el virtualenv `programas-venv`, el directorio que contiene `manage.py` y el archivo WSGI que enlaza esa pestaña con `my_project.wsgi.application`. En **Static files**, mapea `/static/` a la carpeta `staticfiles` del proyecto.

Configura `DJANGO_SECRET_KEY` con una clave privada, `DJANGO_DEBUG=False` y `DJANGO_ALLOWED_HOSTS` con el dominio exacto de la cuenta, por ejemplo `tu_usuario.pythonanywhere.com`. Luego pulsa **Reload** en la pestaña Web. El paso `migrate` completa las tablas de Django; la base incluida ya conserva los cinco programas y la migración de `myapp`.

Referencias: [guía oficial para desplegar un proyecto Django existente](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/) y [configuración de archivos estáticos](https://help.pythonanywhere.com/pages/DjangoStaticFiles/).

`db.sqlite3` se mantiene fuera de `.gitignore` para que la base local con los registros del taller pueda incluirse en el repositorio.
