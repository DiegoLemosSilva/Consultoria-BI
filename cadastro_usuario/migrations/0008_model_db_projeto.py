# Generated by Django 5.1.2 on 2024-11-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_usuario', '0007_delete_cliente_delete_model_db_campanha_produto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_db_projeto',
            fields=[
                ('id_projeto', models.AutoField(primary_key=True, serialize=False)),
                ('nome_projeto', models.CharField(db_column='nome_projeto')),
            ],
            options={
                'db_table': '"br_addidas"."projeto"',
                'managed': False,
            },
        ),
    ]
