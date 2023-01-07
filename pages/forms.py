from django import forms
from voter.models import Voter,Candidate

class VoterUpdateAdmin(forms.ModelForm):
    class Meta:
        model = Voter
        fields = '__all__'
        exclude = ['user','voter_id','school_id','voted']

class CandidateCreateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
        exclude = ['approved','votes']
    
    def clean(self):
        cleaned_data = self.cleaned_data
        cgpa = cleaned_data.get('cgpa')
        position = cleaned_data.get('position')
        
        if position.name.lower() == 'president':
            if cgpa < position.cgpa_requirement:
                self.add_error('cgpa','sorry your CGPA is less than the requirement for this position')
        
        elif position.name.lower() == 'vice president':
            if cgpa < position.cgpa_requirement:
                self.add_error('cgpa','sorry your CGPA is less than the requirement for this position')
        
        elif position.name.lower() == 'secretary general':
            if cgpa < position.cgpa_requirement:
                self.add_error('cgpa','sorry your CGPA is less than the requirement for this position')
        
                