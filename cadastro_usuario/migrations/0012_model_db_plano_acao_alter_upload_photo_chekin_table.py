# Generated by Django 5.1.2 on 2024-12-03 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_usuario', '0011_model_db_estabelecimento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_db_plano_acao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Campanha', models.CharField(max_length=255)),
                ('loja', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('Canal', models.CharField(max_length=255)),
                ('produto', models.CharField(max_length=255)),
                ('quantidade', models.CharField(max_length=255)),
                ('valor_unit', models.CharField(max_length=255)),
            ],
            options={
                'db_table': '"br_addidas"."plano_acao"',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='upload_photo_chekin',
            table='"br_addidas"."chekin"',
        ),
    ]