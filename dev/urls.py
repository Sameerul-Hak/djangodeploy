from django.urls import path
from dev.views import home,particularpost
urlpatterns = [
    path("",home,name="home"),
    path("posts/<str:pk>/",particularpost,name="post")
]
