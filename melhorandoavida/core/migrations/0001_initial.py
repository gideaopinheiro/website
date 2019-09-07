# Generated by Django 2.2.5 on 2019-09-07 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256, null=True)),
                ('username', models.CharField(blank=True, max_length=256, null=True, unique=True)),
                ('ocupation', models.CharField(blank=True, max_length=256, null=True)),
                ('university', models.CharField(blank=True, max_length=256, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
