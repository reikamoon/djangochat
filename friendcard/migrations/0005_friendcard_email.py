# Generated by Django 3.0.2 on 2020-03-05 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendcard', '0004_friendcard_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendcard',
            name='email',
            field=models.EmailField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
