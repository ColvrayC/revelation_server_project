#Debug / Production
DEBUG = False

#Hosts
ALLOWED_HOSTS = ['cyclespresso.fr','www.cyclespresso.fr']

#Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'revelation_db',
        'USER': 'postgres',
        'PASSWORD': '@Nonymous18',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
