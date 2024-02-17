# Generated by Django 4.2.10 on 2024-02-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_cookbook_cover_image_alter_post_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cook_time_hours',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='cook_time_minutes',
            field=models.PositiveIntegerField(default=45),
        ),
        migrations.AddField(
            model_name='post',
            name='prep_time_hours',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='prep_time_minutes',
            field=models.PositiveIntegerField(default=25),
        ),
    ]
