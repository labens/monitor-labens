# Generated by Django 2.2.6 on 2019-10-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('cod', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
                ('id', models.IntegerField()),
            ],
        ),
    ]
