# Generated by Django 4.1.2 on 2022-11-14 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('businessplan', '0002_business1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Business',
            new_name='businessdetail',
        ),
        migrations.DeleteModel(
            name='Business1',
        ),
    ]
