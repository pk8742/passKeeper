# Generated by Django 3.0.6 on 2020-05-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Safe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('website', models.CharField(max_length=64)),
                ('userInfo', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('dateTime', models.DateField()),
            ],
        ),
    ]
