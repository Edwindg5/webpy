#tutorial/urls.py
"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from tutorial import view
from tutorial.view import HomePageView,AboutPageView,CarreraCreateViewPage,CarreraEditViewPage,  CarreraDeleteViewPage, ProfesorCreateView, EmpresaCreateView, EmpresaListView, EmpresaDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', view.index, name='index'),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('carreras/', CarreraCreateViewPage.as_view(), name='carreras'),
    path("carreras/editar/<int:pk>/", CarreraEditViewPage.as_view(), name="carreras_editar"),
    path("carreras/eliminar/<int:pk>/", CarreraDeleteViewPage.as_view(), name="carreras_eliminar"),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="login.html"), name= 'logout'),
    path('crear_profesor/', ProfesorCreateView.as_view(), name='crear_profesor'),
    path('registrar_empresa/', EmpresaCreateView.as_view(), name='registrar_empresa'),
    path('ver_empresa/', EmpresaListView.as_view(), name='ver_empresa'),
    path('eliminar_empresa/<int:pk>/', EmpresaDeleteView.as_view(), name='eliminar_empresa'),
]

