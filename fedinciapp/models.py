from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    CHOICE_GENDER=(
       
            ('M','Male'),
            ('F','Femelle'),
      
    )
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=25,blank=False, default='xyz')
    lastname=models.CharField(max_length=25,blank=False, default='xyz')
    contact=models.IntegerField(blank=False, default='22507070707')
    genre=models.CharField(choices=CHOICE_GENDER, max_length=25,blank=False, default='Male')
    age=models.DateField(default=timezone.now)
    pays=CountryField(blank_label="(Choisissez votre pays)",blank=False, default="COTE D'IVOIRE")
    ville=models.CharField(max_length=125,blank=False, default='ABIDJAN')
    emploi=models.CharField(max_length=125,blank=False, default='INVENTEUR')
    bio=models.TextField(default='Ma biographie...')
    image=models.ImageField(default='default.jpg', upload_to='img_profile')
    def __str__(self):
        return f'Profile de {self.user.username}'