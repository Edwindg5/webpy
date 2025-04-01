#tutorial/urls.py

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from tutorial import view
from tutorial.view import HomePageView,AboutPageView,CarreraCreateViewPage,CarreraEditViewPage,  CarreraDeleteViewPage, ProfesorCreateView, EmpresaCreateView, EmpresaListView, EmpresaDeleteView, BatallasPageView


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
    path('batallas/', BatallasPageView.as_view(), name='batallas'),
    
]

