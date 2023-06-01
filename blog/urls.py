"""
To use the function-based view, uncomment lines 6 and 9 and comment lines 7 and 10
"""

from django.urls import path
# from .views import list_view
from .views import PostListView
urlpatterns = [
    # path('', list_view, name='list-view'),
    path('', PostListView.as_view(), name='list-view'),
]