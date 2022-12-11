# Generated by Django 4.1.4 on 2022-12-10 10:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_book_summary"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="cover",
            field=models.ImageField(
                default=django.utils.timezone.now, upload_to="cover"
            ),
            preserve_default=False,
        ),
    ]