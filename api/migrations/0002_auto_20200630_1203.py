# Generated by Django 2.0.6 on 2020-06-30 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='bookname',
            new_name='book_name',
        ),
    ]