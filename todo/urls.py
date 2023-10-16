
from django.contrib import admin
from django.urls import path
from todo.views import home , login , signup , signout


urlpatterns = [
   path('' , home , name='home' ), 
   path('login/' ,login  , name='login'), 
   path('signup/' , signup ), 
   path('logout/' , signout ), 
]
