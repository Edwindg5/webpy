#tutorial/views.py
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from .models import Carrera
from .vistas import CarreraForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    return HttpResponse("Hello, world. You're at the polls ollaaa.")

class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Carrera
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['my_name'] = ''
        context["lista"] = self.model.objects.all()
        return context
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    

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
        return self.render_to_response(context)
    
    def post(self, request, pk, *args, **kwargs):
        carrera=get_object_or_404(Carrera, pk=pk)
        form = CarreraForm(request.POST, instance=carrera)
        if form.is_valid():
            carrera = form.save()
            return render(request, 'carreras_form.html', {'form': CarreraForm()})
        else:
            return render(request, 'carreras_form.html', {'form': form})

class CarreraDeleteViewPage(TemplateView):
    template_name = 'carreras_form.html'
    def get(self, request, pk, *args, **kwargs):
        carrera=get_object_or_404(Carrera, pk=pk)
        forms = CarreraForm(instance=carrera)
        carrera.delete()
        return redirect('/')
    
    
