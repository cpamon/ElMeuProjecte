from django import forms
from .models import RefMapa

class EntraUrlWMS(forms.Form):
    urlWMS = forms.CharField(label='Url del WMS:', max_length=300)

class CatalegForm(forms.Form):
    nomCercat = forms.CharField(label='Cerca', max_length=100)

class PokemonForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=20)
    tipus = forms.CharField(label='Tipus', max_length=100)
    foto = forms.ImageField(label='Foto')


class RefMapaForm(forms.ModelForm):
    class Meta:
        model = RefMapa
        fields = ['tipus', 'nom', 'descripcio', 'pUrl', 'urlCapabilities', 'foto']

    def __init__(self, *args, **kwargs):
        super(RefMapaForm, self).__init__(*args, **kwargs)
        self.fields['descripcio'].required = False
        self.fields['foto'].required = False
        self.fields['tipus'].widget.attrs['readonly'] = True
        self.fields['urlCapabilities'].required = False
        self.fields['urlCapabilities'].widget.attrs['readonly'] = True

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field
        })


class RefMapaWMSForm(forms.ModelForm):
    class Meta:
        model = RefMapa
        fields = ['tipus', 'nom', 'descripcio', 'pUrl', 'urlCapabilities', 'foto']

    def __init__(self, *args, **kwargs):
        super(RefMapaWMSForm, self).__init__(*args, **kwargs)
        self.fields['descripcio'].required = False
        self.fields['foto'].required = False
        self.fields['tipus'].widget.attrs['readonly'] = True
        self.fields['urlCapabilities'].required = False
        self.fields['urlCapabilities'].widget.attrs['readonly'] = True

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field
        })

class RefMapaWMTSForm(forms.ModelForm):
    class Meta:
        model = RefMapa
        fields = ['tipus', 'nom', 'descripcio', 'pUrl', 'urlCapabilities', 'matrixSet', 'foto']

    def __init__(self, *args, **kwargs):
        super(RefMapaWMTSForm, self).__init__(*args, **kwargs)
        self.fields['descripcio'].required = False
        self.fields['urlCapabilities'].required = False
        self.fields['urlCapabilities'].widget.attrs['readonly'] = True
        self.fields['tipus'].widget.attrs['readonly'] = True

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field
        })


class RefMapaVectorForm(forms.ModelForm):
    class Meta:
        model = RefMapa
        fields = ['tipus', 'nom', 'descripcio', 'pUrl', 'urlCapabilities', 'matrixSet', 'format', 'foto']
    
    def __init__(self, *args, **kwargs):
        super(RefMapaVectorForm, self).__init__(*args, **kwargs)
        self.fields['format'].required = False
        self.fields['descripcio'].required = False
        self.fields['urlCapabilities'].required = False
        self.fields['urlCapabilities'].widget.attrs['readonly'] = True
        self.fields['tipus'].widget.attrs['readonly'] = True

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field
        })

    """ tipus = forms.CharField(label='Tipus', max_length=20)
    nom = forms.CharField(label='Nom', max_length=100)
    pCapes = forms.CharField(label='PCapes', max_length=100)
    pUrl = forms.CharField(label='PUrl', max_length=200)
    urlCapabilities = forms.CharField(label='UrlCapabilities', max_length=200)
    matrixSet = forms.CharField(label='MatrixSet', max_length=30)
    #foto = forms.ImageField(label='Foto') """