# Generated by Django 3.2.4 on 2021-07-16 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/post_photos'),
        ),
    ]
