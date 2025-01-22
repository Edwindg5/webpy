from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return HttpResponse("Hello, world. You're at the polls ollaaa.")

class HomePageView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['my_name'] = 'Fernando'
        context["lista"] = [1,2,3,4,5]
        return context
    
class AboutPageView(TemplateView):
    template_name = 'about.html'