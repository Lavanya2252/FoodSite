from django.urls import path
from . import views

# add this app_name to refer this along with name from 'urls.py' ie. food:details, food:item
app_name = "food"
urlpatterns = [
    path("index", views.index, name="index"),
    path("<int:item_id>", views.details, name='details'),
    path("create_item", views.create_item, name='create_item'),
    path("update_item/<int:id>", views.update_item, name='update_item'),
    path("delete_item/<int:id>", views.delete_item, name='delete_item'),
]