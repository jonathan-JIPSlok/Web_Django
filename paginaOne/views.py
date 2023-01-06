from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("""
    <h1>Olá Mundo!</h1>
    <p>Meu nome é Jonathan Yuri e esse é meu inicio do aprendizado.</p>
    """)
