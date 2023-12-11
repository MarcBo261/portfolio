

from django.urls import path
from AppPrincipal import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('skills/', views.skills, name='skills'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.realisation, name='realisation'),
    path('loisirs/', views.loisir, name='loisir'),
    path('contact/', views.contact, name='contact'),
    path('connexion/', views.connexion, name='connexion'),
    path('signup/',views.signup,name='signup')
]