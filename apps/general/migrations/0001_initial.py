# Generated by Django 4.0.6 on 2022-07-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('online', models.BooleanField(default=True)),
            ],
        ),
    ]
