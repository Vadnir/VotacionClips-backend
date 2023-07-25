from rest_framework import serializers
from .models import Clip, ClipVote


class ClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clip
        fields = '__all__'


class ClipVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClipVote
        fields = '__all__'