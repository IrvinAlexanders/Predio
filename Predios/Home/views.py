from django.shortcuts import render
from django.views import generic

class inicio(generic.TemplateView): 
    template_name = "inicio.html"
   