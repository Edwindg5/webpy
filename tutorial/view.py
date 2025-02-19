#tutorial/views.py
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from .models import Carrera
from django.views import View
from .vistas import CarreraForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from tutorial.forms.profesor_form import ProfesorForm
from tutorial.models.profesor import Profesor
from tutorial.forms.empresa_form import EmpresaForm
from tutorial.models import Empresa
from django.views.generic import ListView
from tutorial.models.empresa import Empresa


def index(request):
    return HttpResponse("Hello, world. You're at the polls ollaaa.")

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_name'] = 'Bienvenido a la plataforma de Carreras'
        context["lista"] = Carrera.objects.all()  # Se usa Carrera.objects.all()
        return context
class ProfesorCreateView(TemplateView):
    template_name = "profesor_form.html"

    def get(self, request, *args, **kwargs):
        form = ProfesorForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Profesor registrado correctamente."})
        return JsonResponse({"success": False, "message": "Error al registrar el profesor."}, status=400)


    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lista"] = Carrera.objects.all()  # Ahora se envían las carreras a about.html
        return context

#@method_decorator(permission_required('tutorial.add_carrera', login_url='/', raise_exception=False), name='dispatch')
class CarreraCreateViewPage(TemplateView):
    template_name = 'carreras_form.html'
    model = Carrera
    def get(self, request, *args, **kwargs):
        form = CarreraForm()
        context={'form':form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = CarreraForm(request.POST)
        if form.is_valid():
            carrera = form.save()
            return render(request, 'carreras_form.html', {'form': CarreraForm()})
        else:
            return render(request, 'carreras_form.html', {'form': form})
        

class CarreraEditViewPage(TemplateView):
    template_name = 'carreras_form.html'
    
    def get(self, request, pk, *args, **kwargs):
        carrera=get_object_or_404(Carrera, pk=pk)
        form = CarreraForm(instance=carrera)
        context={'form':form}
        return self.render_to_response({'form':form, 'has_permission': request.user.has_perm('change_carrera')})
    @method_decorator(permission_required('tutorial.change_carrera', login_url='/', raise_exception=False), name='dispatch')
    def post(self, request, pk, *args, **kwargs):
        carrera=get_object_or_404(Carrera, pk=pk)
        form = CarreraForm(request.POST, instance=carrera)
        if form.is_valid():
            carrera = form.save()
            return render(request, 'carreras_form.html', {'form': CarreraForm()})
        else:
            return render(request, 'carreras_form.html', {'form': form})

class CarreraDeleteViewPage(View):
    def post(self, request, pk, *args, **kwargs):
        carrera = get_object_or_404(Carrera, pk=pk)
        carrera.delete()
        return JsonResponse({"success": True, "message": "Carrera eliminada correctamente."})
    
    
    
    
class EmpresaCreateView(View):
    template_name = "empresa_form.html"

    def get(self, request):
        form = EmpresaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_empresa')  # Redirige a la lista de empresas
        else:
            return render(request, self.template_name, {'form': form, 'errors': form.errors})
        
class EmpresaListView(ListView):
    model = Empresa
    template_name = "empresa.html"
    context_object_name = "empresas"
    
class EmpresaDeleteView(View):
    def post(self, request, pk):
        empresa = get_object_or_404(Empresa, pk=pk)
        empresa.delete()
        return JsonResponse({"success": True, "message": "Empresa eliminada correctamente."})