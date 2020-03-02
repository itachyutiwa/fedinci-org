from django.urls import path
from .import views


urlpatterns=[

    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('nos_institutions', views.nos_institutions, name='nos_institutions'),
    path('videos_et_medias', views.videos_et_medias, name='videos_et_medias'),
    path('contact', views.contact, name='contact'),
    path('profile', views.profile, name='profile'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('devenir_membre', views.devenir_membre, name='devenir_membre'),
    path('evenements', views.evenements, name='evenements'),
    path('protection', views.protection, name='protection'),
    path('rendez_vous', views.rendez_vous, name='rendez_vous'),
    path('inscription', views.inscription, name='inscription'),
    path('connexion', views.connexion, name='connexion'),
    path('member_detail', views.member_detail, name='member_detail'),
    path('prix_et_laureats', views.prix_et_laureats, name='prix_et_laureats'),
    path('a_propos_de_nous', views.a_propos_de_nous, name='a_propos_de_nous'),
]