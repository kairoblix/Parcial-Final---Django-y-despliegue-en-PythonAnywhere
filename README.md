# Taller Django: programas académicos

Proyecto basado en [DesarrolladorSA11/web1_development](https://github.com/DesarrolladorSA11/web1_development). Incluye el modelo Programa, formulario de creación, administrador y base de datos con cinco registros de ejemplo.

Formulario: `/programas/crear/`  
Administrador: `/admin/`

Para ejecutar en PythonAnywhere: instalar `requirements.txt` en un entorno virtual, configurar `my_project.wsgi.application`, ejecutar `python manage.py migrate` y `python manage.py collectstatic`. La base `db.sqlite3` contiene los cinco programas registrados mediante el formulario.

Configura `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False` y `DJANGO_ALLOWED_HOSTS` para tu dominio de PythonAnywhere antes de habilitar el sitio.