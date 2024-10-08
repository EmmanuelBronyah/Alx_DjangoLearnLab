# Generated by Django 5.0.8 on 2024-08-21 19:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bookshelf", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={
                "permissions": [
                    ("can_view", "Can view book"),
                    ("can_create", "Can create book"),
                    ("can_edit", "Can edit book"),
                    ("can_delete", "Can delete book"),
                ]
            },
        ),
    ]
