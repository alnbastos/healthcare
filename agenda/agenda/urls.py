"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('quemsomos/', views.quem_somos),
    path('agendamento/', views.agendamento),
    path('servicos/', views.servicos),
    # login
    path('selectuser/', views.select_user),
    path('selectuser/logincliente/', views.login_cliente),
    # cadastrar
    path('cadastro/cliente/', views.cadastro_cliente, name='aline'),
    path('cadastro/medico/', views.cadastro_medico),
    path('cadastro/clinica/', views.cadastro_clinica),
    # agendar
    path('agendar/', views.agendar),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
