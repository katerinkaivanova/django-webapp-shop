# Generated by Django 2.2 on 2019-05-07 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_shopuserprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopuserprofile',
            old_name='aboutMe',
            new_name='aboutme',
        ),
    ]
