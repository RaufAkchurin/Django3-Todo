# Generated by Django 3.2.12 on 2022-06-30 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoo', '0005_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date_complete',
        ),
        migrations.AddField(
            model_name='todo',
            name='complete',
            field=models.DateField(auto_now_add=True, default='1990-09-11'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='memo',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]