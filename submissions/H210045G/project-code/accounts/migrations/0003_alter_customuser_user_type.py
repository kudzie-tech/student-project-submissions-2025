# Generated by Django 5.1.6 on 2025-03-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_customuser_user_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[("admin", "Admin"), ("Basic User", "Basic User")],
                default="admin",
                max_length=10,
            ),
        ),
    ]
