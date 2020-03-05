# Generated by Django 3.0.2 on 2020-03-05 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendcard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('created', models.DateTimeField(verbose_name='date created')),
                ('home', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Card',
        ),
    ]
