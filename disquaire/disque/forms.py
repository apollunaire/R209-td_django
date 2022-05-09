from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from  django import forms




class DisquaireForm(ModelForm):
    class Meta:
        model = models.Disquaire
        fields = ('nom', 'ville', 'cp', 'num_rue', 'nom_rue', 'num_tel', 'site')
        labels = {
            'nom' : _('Nom'),
            'ville' : _('Ville'),
            'cp' : _('Code Postal'),
            'num_rue' : _('N° de rue'),
            'nom_rue' : _('Nom de la rue'),
            'num_tel' : _('N° de téléphone'),
            'site' : _('Site web')
        }


class DisqueForm(ModelForm):
    class Meta:
        model = models.Disque
        fields = ('magasin', 'titre', 'label', 'artiste', 'date_sortie', 'nb_morceaux', 'genre', 'duree', 'image')
        labels = {
            'magasin': _('Magasin'),
            'titre' : _('Titre'),
            'label' : _('Label'),
            'artiste' : _('Artiste'),
            'date_sortie' : _('Date de sortie'),
            'nb_morceaux' : _('Nombre de morceaux'),
            'genre' : _('Genre'),
            'duree' : _('Durée'),
            'image' : _('Lien d\'une image')
            }

