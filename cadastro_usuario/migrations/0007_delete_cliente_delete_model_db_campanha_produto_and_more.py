# Generated by Django 5.1.2 on 2024-11-19 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_usuario', '0006_model_db_campanha_produto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='model_db_campanha_produto',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]
