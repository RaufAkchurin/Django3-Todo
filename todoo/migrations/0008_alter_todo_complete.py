# Generated by Django 3.2.12 on 2022-07-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoo', '0007_alter_todo_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='complete',
            field=models.DateTimeField(blank=True),
        ),
    ]
