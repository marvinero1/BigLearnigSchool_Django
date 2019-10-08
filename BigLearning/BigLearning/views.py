from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def index(request):
    
    #doc_externo=loader.get_template('inicio.html')

    #plantilla=Template(doc_externo.read())

    #doc_externo.close()

    #contexto=Context()

    #documento=doc_externo.render()

    return render(request, "index.html", None)

def cursos(request):
    return render(request, "cursos.html", None)