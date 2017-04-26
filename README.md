
## Set up app
- set the project's setting.py
add 'queen.apps.QueenConfig' into INSTALLED_APPS

- set the project's urls.py
add url patterns. like this:

    urlpatterns = [
    url(r'^queen/', include('queen.urls')),
    url(r'^admin/', admin.site.urls),
    ]


- set db

`./manage.py makemigrations queen`
`./manage.py migrate`
