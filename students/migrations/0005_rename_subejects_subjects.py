# Generated by Django 5.1.4 on 2025-01-04 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0004_primarystatus_secondarystatus"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Subejects",
            new_name="Subjects",
        ),
    ]
