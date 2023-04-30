# Generated by Django 4.2 on 2023-04-30 05:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("restapp", "0004_todo_user_alter_todo_uid_alter_todotiming_uid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="uid",
            field=models.UUIDField(
                default=uuid.UUID("d4459f45-8a91-418c-9cf1-076a51868689"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="todotiming",
            name="uid",
            field=models.UUIDField(
                default=uuid.UUID("d4459f45-8a91-418c-9cf1-076a51868689"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
