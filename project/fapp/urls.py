from django.urls import path
from .views import home,add_laptop,display,update,delete

urlpatterns=[
    path('',home,name='home'),
    path('add_laptop/',add_laptop,name='add_laptop'),
    path('display/',display,name='display'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
]