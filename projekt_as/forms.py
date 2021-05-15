from django import forms
from .models import Post, Komentarz, KomentarzX


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('tytul', 'tresc', 'id_autora')

        widgets = {
            'tytul': forms.TextInput(attrs={'class': 'form-control'}),
            'tresc': forms.Textarea(attrs={'class': 'form-control'}),
            'id_autora': forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'user', 'type':'hidden'})
        }

class KomentarzForm(forms.ModelForm):
    class Meta:
        model = Komentarz
        fields = ('tresc', 'id_user')

        widgets = {
            'tresc': forms.Textarea(attrs={'class':'form-control'}),
            'id_user': forms.TextInput(attrs={'class':'form-control', 'id':'user', 'type':'hidden'}),
        }

class KomentarzXForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'pisz...','rows':'4','cols':'50'}))
    class Meta:
        model = KomentarzX
        fields = ('content',)
