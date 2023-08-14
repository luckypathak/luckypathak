from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView

class Index(TemplateView):
    template_name = 'index.html'

class Aboutus(TemplateView):
    template_name = 'about-us.html'

class Service(TemplateView):
    template_name = 'service.html'

class OurTeam(TemplateView):
    template_name = 'our-team.html'

class Project(TemplateView):
    template_name = 'project.html' 

class Contact(TemplateView):
    template_name = 'contact.html'
 
 
