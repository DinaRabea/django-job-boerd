from django.urls import path , include

from . import views
urlpatterns = [
    path('', views.all_jobs),
    path('<int:id>', views.show_job)

]