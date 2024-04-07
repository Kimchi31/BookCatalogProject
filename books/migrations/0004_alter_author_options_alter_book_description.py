# Generated by Django 4.2.10 on 2024-03-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0003_favorites"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"verbose_name": "Author", "verbose_name_plural": "Авторы"},
        ),
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
    ]