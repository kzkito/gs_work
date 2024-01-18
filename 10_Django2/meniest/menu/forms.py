from django import forms

class TranslationForm(forms.Form):

    sentence = forms.CharField(label='translation...', widget=forms.Textarea(), required=True)
