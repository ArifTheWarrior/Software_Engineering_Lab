# Generated by Django 4.1.7 on 2023-03-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
