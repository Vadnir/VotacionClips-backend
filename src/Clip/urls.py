from django.urls import path, include
from rest_framework import routers
from .views import ClipListView, ClipVoteListView, ClipVoteView

list_views = [
    path("clip/", ClipListView.as_view()),
    path("voteclip/", ClipVoteListView.as_view())
]

urlpatterns = [
    path('list/', include(list_views)),
    path('vote/', ClipVoteView.as_view()),
]
