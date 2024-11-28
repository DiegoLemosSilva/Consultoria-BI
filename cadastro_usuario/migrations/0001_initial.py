# Generated by Django 5.1.2 on 2024-11-04 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('idade', models.IntegerField()),
            ],
            options={
                'db_table': 'br_addidas.cadastro_usuario_cliente',
                'managed': False,
            },
        ),
    ]