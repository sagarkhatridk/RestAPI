# Generated by Django 4.2 on 2023-04-30 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("restapp", "0006_remove_todo_user_alter_todo_uid_alter_todotiming_uid"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="uid",
            field=models.UUIDField(
                default=uuid.UUID("db593935-9910-4749-a96d-e9ed6b3da654"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="todotiming",
            name="uid",
            field=models.UUIDField(
                default=uuid.UUID("db593935-9910-4749-a96d-e9ed6b3da654"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]