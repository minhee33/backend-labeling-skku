# Generated by Django 4.2.6 on 2023-11-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_rename_account_id_label_account"),
    ]

    operations = [
        migrations.AddField(
            model_name="label",
            name="color_code",
            field=models.CharField(default="#171718", max_length=100),
        ),
    ]
