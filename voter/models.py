from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

class Faculty(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name[:]

class Department(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Voter(models.Model):
    GENDER = (
        ('male','MALE'),
        ('female','FEMALE'),
        )
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    voter_id = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True,choices=GENDER)
    school_id = models.ImageField(null=True,blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True,blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE,null=True,blank=True)
    verified = models.BooleanField(default=False)
    voted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.full_name

class Candidate(models.Model):
    GENDER = (
        ('MALE','male'),
        ('FEMALE',' female'),
        )
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50,null=True,blank=True,choices=GENDER)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True,blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE,null=True,blank=True)
    position = models.ForeignKey('Position',on_delete=models.CASCADE,null=True,blank=True)
    cgpa = models.FloatField(null=True,blank=True)
    school_id = models.ImageField(null=True,blank=True)
    phone_number = models.PositiveIntegerField(null=True,blank=True)
    current_result_slip = models.ImageField(null=True,blank=True)
    approved = models.BooleanField(default=False)
    votes = models.PositiveIntegerField(null=True,blank=True,default=0)

    def __str__(self):
        return self.user.full_name
        
class Position(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    cgpa_requirement = models.FloatField(null=True,blank=True)
    
    def __str__(self):
        return self.name


def voter_creation_signal(sender,instance,created,*args,**kwargs):
    if created:
        Voter.objects.create(
            user = instance,
            voter_id = f'VID/{instance.reg[5:]}'
        )
post_save.connect(voter_creation_signal,sender=User)