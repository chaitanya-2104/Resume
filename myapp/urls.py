from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('home/',views.Show,name='homes'),
     path('<int:pk>',views.CandidatesView.as_view(),name='candidate'),
  

]
