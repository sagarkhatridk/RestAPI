# Generated by Django 4.2 on 2023-04-30 10:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("restapp", "0008_alter_todo_uid_alter_todotiming_uid"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimingTodo",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.UUID("e5e9d82b-015a-4ef9-a948-51d8e1c49c00"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateField(auto_now=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("timing", models.DateField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="todo",
            name="uid",
            field=models.UUIDField(
                default=uuid.UUID("e5e9d82b-015a-4ef9-a948-51d8e1c49c00"),
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.DeleteModel(
            name="TodoTiming",
        ),
        migrations.AddField(
            model_name="timingtodo",
            name="todo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="restapp.todo"
            ),
        ),
    ]