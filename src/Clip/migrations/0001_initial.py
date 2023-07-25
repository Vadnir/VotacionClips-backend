# Generated by Django 4.2.3 on 2023-07-22 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('url', models.URLField(max_length=1000)),
                ('votes', models.BigIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clip.category')),
            ],
            options={
                'verbose_name': 'Clip',
                'verbose_name_plural': 'Clips',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='ClipVote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clip.category')),
                ('clip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clip.clip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ClipVote',
                'verbose_name_plural': 'ClipVotes',
                'ordering': ['-user'],
            },
        ),
    ]
