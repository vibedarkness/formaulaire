# Generated by Django 4.1.5 on 2023-05-26 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="fulluser",
            name="user_type",
            field=models.CharField(
                choices=[(1, "ADMIN"), (2, "STAFF")], default=1, max_length=20
            ),
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("address", models.TextField()),
                ("telephone", models.CharField(max_length=150)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "admin",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Admin",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "admin",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
