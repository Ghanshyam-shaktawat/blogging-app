# Generated by Django 4.0.6 on 2022-08-03 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about',
            field=models.CharField(default='I have nothing to say...', max_length=255),
        ),
    ]
