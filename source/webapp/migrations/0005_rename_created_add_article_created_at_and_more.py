# Generated by Django 4.1.2 on 2022-11-01 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='created_add',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='updated_add',
            new_name='updated_at',
        ),
    ]