from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('name', 'phone', 'email', 'gender', 'carrier')
        labels ={
            'name': 'name',
            'email':'email',
        }
        #placeholders
        widget = {
            'name' : forms.TimeInput(attrs={'placeholder':'Your name'}),
            'phone' : forms.TimeInput(attrs={'placeholder':'Your phone'}),
            'email' : forms.TimeInput(attrs={'placeholder':'Your email'}),
        }
        
    
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)
        self.fields['gender'].choices = [('', 'select a gender'),] + list(self.fields['gender'].choices)[1:]
        self.fields['carrier'].empty_label = "self an option"
        self.fields['email'].required = True
