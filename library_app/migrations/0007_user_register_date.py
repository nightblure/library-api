# Generated by Django 4.1.4 on 2022-12-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0006_alter_user_reader_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='register_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]