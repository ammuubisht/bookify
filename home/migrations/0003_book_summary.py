# Generated by Django 4.1.4 on 2022-12-10 10:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_genre_remove_book_genre_book_genre"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="summary",
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
