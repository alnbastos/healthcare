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
    path('login/', views.login_user),
    path('login/submit', views.submit_user),
    # logout
    path('logout/', views.logout_user),
    # perfis
    path('perfil/cliente/', views.perfil_cliente, name='perfil-cliente'),
    path('perfil/medico/', views.perfil_medico, name='perfil-medico'),
    path('perfil/clinica/', views.perfil_clinica, name='perfil-clinica'),
    # cadastrar
    path('cadastro/cliente/', views.cadastro_cliente),  # , name='aline'),
    path('cadastro/medico/', views.cadastro_medico),
    path('cadastro/clinica/', views.cadastro_clinica),
    # após cadastro
    path('cadastro/cliente/ok/', views.ok_cliente),
    path('cadastro/medico/ok/', views.ok_medico),
    path('cadastro/clinica/ok/', views.ok_clinica),
    # agendar
    path('agendar/', views.agendar),
    path('agendar/ok/', views.ok_agendar),
    path('ajax/load-clinica/', views.load_clinica, name='ajax_load_clinica'),
    path('ajax/load-medico/', views.load_medico, name='ajax_load_medico'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
