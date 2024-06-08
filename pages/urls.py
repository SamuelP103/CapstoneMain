from django.urls import path 
from .views import HomePageView, AboutPageView
from .views import Create, ListPosts, PostDetail



urlpatterns = [
    path("", HomePageView.as_view(), name="home"),

    path("about/", AboutPageView.as_view(), name="about"),
    path('create', Create.as_view(), name='create'),
    path('list', ListPosts.as_view(), name='list'),
    path('detail/<int:pk>', PostDetail.as_view(), name='detail')
]