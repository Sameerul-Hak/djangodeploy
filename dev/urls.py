from django.urls import path
from dev.views import home
urlpatterns = [
    path("",home,name="home")
]
