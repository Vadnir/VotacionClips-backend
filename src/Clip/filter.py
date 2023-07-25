from .models import Clip, ClipVote
from django_filters import rest_framework as filters


class ClipFilter(filters.FilterSet):

    class Meta:
        model = Clip
        fields = {
            'category__name': ['contains', 'exact'],
            'name': ['exact', 'contains'],
        }


class ClipVoteFilter(filters.FilterSet):

    class Meta:
        model = ClipVote
        fields = {
            'user__username': ['contains', 'exact'],
            'category__name': ['contains', 'exact']
        }