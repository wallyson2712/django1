# Generated by Django 3.0.3 on 2020-02-23 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='nome')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
            ],
        ),
    ]
