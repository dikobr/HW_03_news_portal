from django.urls import path
from .views import PostsList, PostDetail, NewsSearch

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', NewsSearch.as_view(), name='post_search'),

]
