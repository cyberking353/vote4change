from django import forms
from .models import Voter

class VoterUpdateForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = ['gender','school_id','department','faculty']