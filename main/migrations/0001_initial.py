# Generated by Django 4.0.6 on 2022-07-23 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('snippets', models.CharField(max_length=200)),
                ('body', tinymce.models.HTMLField()),
                ('slug', models.SlugField(help_text='This field take uer input', max_length=80, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
