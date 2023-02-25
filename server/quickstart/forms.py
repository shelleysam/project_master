from django import forms
from quickstart.models import formsModel

class UploadForm(forms.ModelForm):
    class Meta:
        model = formsModel
        fields = ('title', 'pdf',)
