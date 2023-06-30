# Generated by Django 4.2.2 on 2023-06-25 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookstoremodel',
            fields=[
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('ISBN', models.IntegerField(primary_key=True, serialize=False)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('Histry', 'Histry'), ('Science', 'Science'), ('Thenology', 'Thenology'), ('Lifestyle', 'Lifestyle')], max_length=20)),
                ('availability_status', models.BooleanField(default=True)),
            ],
        ),
    ]
