# Generated by Django 5.1.2 on 2024-11-13 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_usuario', '0003_checkini_delete_checkininstalacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='campanha',
            fields=[
                ('id_campanha', models.AutoField(primary_key=True, serialize=False)),
                ('nome_campanha', models.TextField(db_column='nome_campanha')),
            ],
            options={
                'db_table': '"br_addidas"."campanha"',
                'managed': False,
            },
        ),
    ]