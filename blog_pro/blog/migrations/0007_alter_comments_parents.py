# Generated by Django 4.0.2 on 2023-01-06 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_options_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='parents',
            field=models.ForeignKey(blank=True, null=None, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.comments'),
        ),
    ]
