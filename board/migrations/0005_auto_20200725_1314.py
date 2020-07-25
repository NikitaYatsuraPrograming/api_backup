# Generated by Django 3.0.8 on 2020-07-25 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='publication',
        ),
        migrations.AddField(
            model_name='publications',
            name='comments',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='board.Comments', verbose_name='Комментарий'),
        ),
    ]