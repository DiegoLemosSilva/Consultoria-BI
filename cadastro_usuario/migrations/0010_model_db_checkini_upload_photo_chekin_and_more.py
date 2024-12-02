# Generated by Django 5.1.2 on 2024-12-02 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_usuario', '0009_model_db_cardapio'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_db_CheckinI',
            fields=[
                ('chekin_id', models.AutoField(primary_key=True, serialize=False)),
                ('estabelecimento', models.TextField(db_column='estabelecimento')),
                ('img', models.TextField(db_column='img')),
                ('cidade', models.TextField(db_column='cidade')),
                ('estado', models.TextField(db_column='estado')),
                ('tipo_servico', models.TextField(db_column='tipo_servico')),
                ('nome_campanha', models.IntegerField(db_column='nome_campanha')),
                ('nome_produto', models.TextField(db_column='nome_produto')),
                ('tipo', models.TextField(db_column='tipo')),
                ('canal', models.TextField(db_column='canal')),
            ],
            options={
                'db_table': '"br_addidas"."chekin"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='upload_photo_chekin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='photos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CheckinI',
        ),
        migrations.DeleteModel(
            name='model_db_campanha',
        ),
        migrations.DeleteModel(
            name='model_db_projeto',
        ),
    ]
