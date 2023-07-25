from django.db import models
from django.contrib.auth.models import User
import uuid


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-name']

    def __str__(self):
        return f"Category(Name={self.name})"


class Clip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=64)
    url = models.URLField(max_length=1000)
    votes = models.BigIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'Clip'
        verbose_name_plural = 'Clips'
        ordering = ['-name']

    def __str__(self):
        return f"Clip(Name={self.name}, votes={self.votes}, Category={self.category}, url={self.url})"


class ClipVote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'ClipVote'
        verbose_name_plural = 'ClipVotes'
        ordering = ['-user']

    def __str__(self):
        return f"ClipVote(User={self.user}, Clip={self.clip}, Category={self.category})"
