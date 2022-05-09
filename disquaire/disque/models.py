from django.db import models
from django import forms
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
GENRE_OPTION = (
        ('Non précisé','Non précisé'),
        ('Rock','Rock'),
        ('Jazz','Jazz'),
        ('Techno','Techno'),
        ('Electro','Electro'),
        ('Indie rock','Indie rock'),
        ('Pop','Pop'),
        ('Métal','Métal'),
        ('Classique', 'Classique'),
    )
class Disquaire(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    cp = models.IntegerField(blank=False)
    nom_rue = models.CharField(max_length=100)
    num_rue = models.IntegerField(blank=False)
    num_tel = PhoneNumberField(blank=True)
    site = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nom} à {self.ville}"

    def dico(self):
        return {'nom': self.nom, 'ville': self.ville, 'nom_rue': self.nom_rue, 'num_rue': self.num_rue, 'num_tel':self.num_tel, 'site':self.site}

class Disque(models.Model):
    magasin = models.ForeignKey(Disquaire, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    artiste = models.CharField(max_length=100)
    date_sortie = models.DateField(blank=True, null=True)
    nb_morceaux = models.IntegerField(blank=False)
    genre = models.CharField(max_length=15, verbose_name="Genre", choices=GENRE_OPTION, default='NON_PRECISE')
    duree = models.DurationField("HH: MM: SS")
    image = models.URLField(blank=True)

    def __str__(self):
        return f"{self.titre} de {self.artiste} sorti le {self.date_sortie} chez {self.label} comprend {self.nb_morceaux} morceaux pour une durée totale de {self.duree}."

    def dico(self):
        return {'magasin': self.magasin, 'titre': self.titre, 'label': self.label, 'artiste': self.artiste, 'date_sortie': self.date_sortie, 'nb_morceaux': self.nb_morceaux, 'duree': self.duree, 'image': self.image}

    @classmethod
    def recup_option(cls):
        return dict(cls.GENRE_OPTION).get(cls.genre)
