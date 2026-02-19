from django.urls import path
from . import views
urlpatterns = [
    path("create_service/",views.create_service,name="create_service"),
    path("service_list/",views.service_list,name="service_list"),
    path("update_service/<int:id>/",views.update_service,name="update_service"),
    path("delete_service/<int:id>/",views.delete_service,name="delete_service"),
]