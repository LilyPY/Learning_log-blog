# Generated by Django 3.2.6 on 2021-08-29 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=56)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]