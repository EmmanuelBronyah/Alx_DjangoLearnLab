# Generated by Django 5.0.8 on 2024-08-21 20:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bookshelf", "0002_alter_book_options"),
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
                    ("can_list", "Can list book"),
                ]
            },
        ),
    ]
