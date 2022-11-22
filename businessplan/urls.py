from django.urls import path
from .import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('signup/',views.Signup,name="signup"),
    path('aboutus/',views.Aboutus,name="aboutus"),
    path('literacy/',views.Literacy,name="literacy"),

    path('business/',views.Business,name="business"),
    path('resources/',views.Resources,name="resources"),
    path('personnel/',views.Personnel,name="personnel"),
    path('market/',views.Market,name="market"),
    path('competitor/',views.Competitor,name="competitor"),
     path('oportunity/',views.Oportunity,name="oportunity"),
    path('strategy/',views.Strategy,name="strategy"),
    path('finance/',views.Finance,name="finance"),



]