from django.urls import path , include

from . import views
urlpatterns = [
    path('', views.all_jobs , name='jobs'),
    path('<str:slug>', views.show_job , name='job')

]