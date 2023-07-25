from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Clip, ClipVote, Category
from .serializer import ClipSerializer, ClipVoteSerializer
from .filter import ClipFilter, ClipVoteFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


class ClipListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Clip.objects.all()
    serializer_class = ClipSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ClipFilter


class ClipVoteListView(generics.ListAPIView):
    queryset = ClipVote.objects.all()
    serializer_class = ClipVoteSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ClipVoteFilter


class ClipVoteView(generics.CreateAPIView, generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ClipVote.objects.all()
    serializer_class = ClipVoteSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if not 'clip_uuid' in data.keys():
            return Response(status=401)

        clip = Clip.objects.filter(id=data['clip_uuid'])
        if len(clip.values()) < 1:
            return Response(status=404)
        clip = clip[0]

        if clip.category in [i.category for i in ClipVote.objects.filter(user=request.user)]:
            clip_vote = ClipVote.objects.filter(category=clip.category)[0]
            clip_vote.clip = clip
        else:
            clip_vote = ClipVote(user=request.user, category=clip.category, clip=clip)

        clip_vote.save()
        return Response(201)

    def destroy(self, request, *args, **kwargs):
        data = request.data
        if not 'clip_uuid' in data.keys():
            return Response(status=401)

        clip = Clip.objects.filter(id=data['clip_uuid'])
        if not clip:
            return Response(status=404)
        clip = clip[0]

        vote_clip = ClipVote.objects.filter(user=request.user, clip=clip)
        if not vote_clip:
            return Response(status=403)
        vote_clip[0].delete()

        return Response(status=201)




