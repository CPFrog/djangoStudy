# Generated by Django 4.0.2 on 2022-03-08 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='voter',
            field=models.ManyToManyField(related_name='answer_voter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='voter',
            field=models.ManyToManyField(related_name='question_voter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_author', to=settings.AUTH_USER_MODEL),
        ),
    ]
