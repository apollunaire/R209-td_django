from django.shortcuts import render
from .forms import LivreForm
from  . import models
from django.http import HttpResponseRedirect


# Create your views here.


def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
            livre = form.save()
            return render(request, "secondapp/affiche.html", {"livre" : livre})
        else:
            return render(request, "secondapp/ajout.html", {"form" : form})
    else:
        form = LivreForm()
        return render(request, "secondapp/ajout.html", {"form" : form})


def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        #return render(request, "secondapp/affiche.html", {"livre" : livre})
        return HttpResponseRedirect("/secondapp/all")
    else:
        return render(request, "secondapp/ajout.html", {"form" : lform})


def all(request):
    liste = list(models.Livre.objects.all())
    return render(request, "secondapp/all.html", {"liste" : liste})


def affiche(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request, "secondapp/affiche.html", {"livre" : livre})


def update(request, id):
    livre = models.Livre.objects.get(pk=id)
    lform = LivreForm(livre.dico())
    return render(request, "secondapp/update.html", {"form": lform, "id" : id})


def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False)
        livre.id = id
        livre.save()
        return HttpResponseRedirect("/secondapp/all")
    else:
        return render(request, "secondapp/update.html", {"form": lform, "id": id})


def delete(request, id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/secondapp/all")
