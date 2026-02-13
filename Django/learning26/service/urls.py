from django.urls import path
from . import views
urlpatterns = [
    path("createservice/",views.CreateService,name="createservice"),
    path("servicelist/",views.servicelist,name="servicelist"),
    path("updateservice/<int:id>/",views.updateservice,name="updateservice"),
    path("deleteservice/<int:id>/",views.deleteservice,name="deleteservice"),
]