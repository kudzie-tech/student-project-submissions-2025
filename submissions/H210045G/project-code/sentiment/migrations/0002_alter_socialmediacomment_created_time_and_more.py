# Generated by Django 5.1.6 on 2025-04-02 10:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sentiment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="socialmediacomment",
            name="created_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="socialmediapost",
            name="created_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
