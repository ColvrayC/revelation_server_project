from django.contrib import admin
from django.urls import path
from revelation_server_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('passwords', views.passwords_view, name='passwords'),
    path('cookies', views.cookies_view, name='cookies'),
]
