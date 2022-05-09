from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "myfirstapp/index.html")

def formulaire(request):
    return render(request, "myfirstapp/formulaire.html")

def formulaire2(request):
    return render(request, "myfirstapp/formulaire2.html")

def bonjour(request):
    nom = request.GET["nom"]
    prenom = request.GET["prenom"]
    age = request.GET["age"]
    return render(request, "myfirstapp/bonjour.html", {"nom": nom, "prenom": prenom, "age": age})

def main(request):
    return render(request, "myfirstapp/main.html")