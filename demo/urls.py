from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path("",views.index,name="home"),
    path("contact/",views.contact,name="ContactUS"),

    # for iit
    path("iit/",views.iit,name="iit"),
    path("iit2/",views.iit2,name="iit2"),
    
    # for nit
    path("nit/",views.nit,name="nit"),
    path("nit2/",views.nit2,name="nit2"),
    
    # for iiit
    path("iiit/",views.iiit,name="iiit"),
    path("iiit2/",views.iiit2,name="iiit2"),

    # for iiit
    path("jee/",views.jee,name="jee"),
    path("jee2/",views.jee2,name="jee2"),

]