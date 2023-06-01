from django.urls import path
# from .views import list_view
from .views import PostListView
urlpatterns = [
    # path('', list_view, name='list-view'),
    path('', PostListView.as_view(), name='list-view'),
]