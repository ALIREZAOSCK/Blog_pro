# Generated by Django 4.0.2 on 2023-01-06 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comments_parents'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
