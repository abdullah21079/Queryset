# Generated by Django 4.2 on 2024-04-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('username', models.CharField(max_length=70)),
                ('useremail', models.EmailField(max_length=70)),
                ('userpass', models.CharField(max_length=70)),
            ],
        ),
    ]
