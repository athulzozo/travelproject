from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.demo,name='demo'),
    path('credentials/',include('credentials.urls'))
    #path('about/',views.about,name='about'),
    #path('contact/',views.contact,name='contact'),
    #path('add/',views.addition,name="addition")
]
