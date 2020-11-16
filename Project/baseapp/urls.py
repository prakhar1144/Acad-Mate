from django.urls import path
from .views import Home, Syllabus, Eresources, Qpaper, Contributors, Faq

urlpatterns = [

path('', Home.as_view() , name= 'home'),
path('syllabus/', Syllabus.as_view() , name= 'syllabus'),
path('eresources/', Eresources.as_view() , name= 'eresources'),
path('qpaper/', Qpaper.as_view() , name= 'qpaper'),
path('contributor/', Contributors.as_view() , name= 'contributors'),
path('faq/', Faq.as_view(), name='faq'),

]