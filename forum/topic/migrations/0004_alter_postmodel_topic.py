# Generated by Django 3.2.7 on 2021-09-28 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("topic", "0003_topicmodel_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postmodel",
            name="topic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="topic.topicmodel",
            ),
        ),
    ]