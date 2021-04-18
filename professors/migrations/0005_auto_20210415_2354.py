# Generated by Django 3.1.7 on 2021-04-15 15:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0004_class_professor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='class_section',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='unique_code',
            field=models.CharField(default=uuid.uuid4, max_length=36, null=True, unique=True),
        ),
    ]