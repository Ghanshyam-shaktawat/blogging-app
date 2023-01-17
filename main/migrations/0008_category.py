# Generated by Django 4.0.6 on 2022-07-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_category_alter_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate', models.CharField(max_length=125, unique=True, verbose_name="Post's Category")),
            ],
        ),
    ]
