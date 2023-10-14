from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,TemplateView,DetailView,CreateView

from app.models import School

class Home(TemplateView):
    template_name='app/home.html'


class SchoolList(ListView):
    model=School
    context_object_name='schools'


class SchoolDetail(DetailView):
    model=School
    context_object_name='schoolobj'


class SchoolCreate(CreateView):
    model=School
    fields='__all__'

    