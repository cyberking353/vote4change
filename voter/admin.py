from django.contrib import admin
from .models import Voter,Position,Candidate,Department,Faculty
from django.contrib.admin import ModelAdmin


class CustomVoterAdmin(ModelAdmin):
    model = Voter
    list_display = ['id','voter_id','verified']



admin.site.register(Voter,CustomVoterAdmin)
admin.site.register(Position)
admin.site.register(Candidate)
admin.site.register(Department)
admin.site.register(Faculty)