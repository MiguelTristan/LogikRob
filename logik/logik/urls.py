"""logik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from logikApp import views
# from django.contrib.auth import views as auth_views
# Media archivos del usuario
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='home'),
    path('acerca_de', views.acerca, name='about'),
    path('portafolio', views.portfolio, name='portfolio'),
    path('lenguajes_para_aprender', views.aprende, name='aprende'),

    # Paths de auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    # el 'document_root' es para decir donde los busca y el 'MEDIA_URL' es donde los sirve
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
