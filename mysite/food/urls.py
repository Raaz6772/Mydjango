from .import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path("index/",views.index,name="index"),
    path("it/",views.it,name="it"),
    path("<int:item_id>/",views.detail,name="detail"),
    path("add/",views.create_form,name="create_form"),
    path("update/<int:id>/",views.update_item,name='update_item'),
    path("delete/<int:id>/",views.delete_item,name="delete_item"),
    ]