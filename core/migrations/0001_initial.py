# Generated by Django 4.2.5 on 2024-04-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
    ]
