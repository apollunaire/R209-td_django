from django.shortcuts import render
from .forms import DisqueForm, DisquaireForm
from . import models
from django.http import HttpResponseRedirect


####################################

def index(request):
    return render(request, "disque/index.html")

def main(resquest):
    liste = models.Disquaire.objects.all()
    return render(resquest, 'disque/main.html', {"liste" : liste})



####### DISQUES #######

def ajout(request, id):
    form = DisqueForm()
    return render(request, "disque/ajout.html", {"form":form, "id":id})


def traitement(request, id):
    disquaire = models.Disquaire.objects.get(pk=id)
    lform = DisqueForm(request.POST)
    if lform.is_valid():
        disque = lform.save(commit=False)
        disque.magasin = disquaire
        disque.magasin_id = id
        disque.save()
        return HttpResponseRedirect("/disque/main")
    else:
        return render(request, "disque/ajout.html", {"form" : lform})


def all(request):
    liste = models.Disque.objects.all()
    return render(request, "disque/all.html", {"liste": liste})


def affichedisque(request, id):
    disque = models.Disque.objects.get(pk=id)
    return render(request, "disque/affichedisque.html", {"disque" : disque})


def update(request, id):
    disque = models.Disque.objects.get(pk=id)
    lform = DisqueForm(disque.dico())
    return render(request, "disque/update.html", {"form": lform, "id" : id})


def traitementupdate(request, id):
    disquaire = models.Disquaire.objects.get(pk=id)
    lform = DisqueForm(request.POST)
    if lform.is_valid():
        disque = lform.save(commit=False)
        disque.magasin = disquaire
        disque.magasin_id = id
        disque.save()
        return HttpResponseRedirect("/disque/main/")
    else:
        return render(request, "disque/update.html", {"form": lform, "id": id})


def delete(request, id):
    disque = models.Disque.objects.get(pk=id)
    disque.delete()
    return HttpResponseRedirect("/disque/main")


def disques(request):
    liste = models.Disque.objects.all()
    return render(request, "disque/disques.html", {"liste": liste})


####### DISQUAIRES #######

def ajoutdisquaire(request):
    if request.method == "POST":
        form = (request)
        if form.is_valid():
            disquaire = form.save()
            return render(request, "disque/affichedisquaire.html", {"disquaire" : disquaire})
        else:
            return render(request, "disque/ajoutdisquaire.html", {"form" : form})
    else:
        form = DisquaireForm()
        return render(request, "disque/ajoutdisquaire.html", {"form" : form})


def traitementdisquaire(request):
    lform = DisquaireForm(request.POST)
    if lform.is_valid():
        disquaire = lform.save()
        return HttpResponseRedirect("/disque/main")
    else:
        return render(request, "disque/ajoutdisquaire.html", {"form" : lform})


def alldisquaire(request):
    liste = models.Disquaire.objects.all()
    return render(request, "disque/main.html", {"liste" : liste})


def affichedisquaire(request, id):
    disquaire = models.Disquaire.objects.get(pk=id)
    liste = models.Disque.objects.all()
    return render(request, "disque/affichedisquaire.html", {"disquaire" : disquaire, "liste": liste})


def updatedisquaire(request, id):
    disquaire = models.Disquaire.objects.get(pk=id)
    lform = DisquaireForm(disquaire.dico())
    return render(request, "disque/updatedisquaire.html", {"form": lform, "id" : id})


def traitementupdatedisquaire(request, id):
    lform = DisquaireForm(request.POST)
    if lform.is_valid():
        disquaire = lform.save(commit=False)
        disquaire.id = id
        disquaire.save()
        return HttpResponseRedirect("/disque/main")
    else:
        return render(request, "disque/updatedisquaire.html", {"form": lform, "id": id})


def deletedisquaire(request, id):
    disquaire = models.Disquaire.objects.get(pk=id)
    disquaire.delete()
    return HttpResponseRedirect("/disque/main")