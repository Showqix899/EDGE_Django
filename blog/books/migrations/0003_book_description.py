# Generated by Django 5.1.1 on 2024-10-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_is_published_alter_book_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]
