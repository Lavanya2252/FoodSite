from django.urls import path
from . import views

# add this app_name to refer this along with name from 'urls.py' ie. food:details, food:item
app_name = "food"
urlpatterns = [
    path("index", views.index, name="index"),
    path("<int:item_id>", views.details, name='details'),
]