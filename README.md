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

## Despliegue

Configura el WSGI de PythonAnywhere para importar `my_project.wsgi.application`, instala `requirements.txt` en el entorno virtual asociado, ejecuta `python manage.py migrate`, configura los archivos estáticos con `python manage.py collectstatic` y agrega el dominio `*.pythonanywhere.com` a `DJANGO_ALLOWED_HOSTS`. Define `DJANGO_SECRET_KEY` como variable de entorno y `DJANGO_DEBUG=False`.

`db.sqlite3` se mantiene fuera de `.gitignore` para que la base local con los registros del taller pueda incluirse en el repositorio.
