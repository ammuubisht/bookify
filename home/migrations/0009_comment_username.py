# Generated by Django 4.1.4 on 2022-12-11 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_remove_comment_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="username",
            field=models.CharField(default="User", max_length=100),
        ),
    ]