from django.db import models
import os

class model_db_CheckinI(models.Model):
    
    """ chekin_id = models.AutoField(primary_key=True)  # Define chekin_id como a chave primária
    estabelecimento = models.TextField(db_column='estabelecimento')
    img =  models.TextField(db_column='img')
    cidade = models.TextField(db_column='cidade')
    estado = models.TextField(db_column='estado')
    tipo_servico = models.TextField(db_column='tipo_servico')
    nome_campanha = models.IntegerField(db_column='nome_campanha')
    nome_produto = models.TextField(db_column='nome_produto')
    tipo = models.TextField(db_column='tipo')
    canal = models.TextField(db_column='canal') """

    chekin_id = models.AutoField(primary_key=True)  # Define chekin_id como a chave primária
    data = models.DateField(db_column='data')
    protocolo =  models.CharField(db_column='protocolo')  
    tipo = models.CharField(db_column='tipo')
    nome_campanha = models.CharField(db_column='nome_campanha')
    tipo_servico = models.CharField(db_column='tipo_servico')
    nome_produto = models.CharField(db_column='nome_produto')
    canal = models.TextField(db_column='canal')
    estabelecimento = models.TextField(db_column='estabelecimento')
    img =  models.ImageField(db_column='img')
      


    class Meta:
        db_table = '"br_addidas"."chekin"'  # Nome da tabela existente
        managed = False  # Impede que o Django gerencie a tabela


    @classmethod
    def get_by_instalacao(cls,tipo,nome_tipo_servico,canal, nome_campanha,nome_produto):
        # Verifique se ambos os filtros têm valores antes de realizar a consulta
        if tipo and nome_tipo_servico and canal and nome_campanha == '':
            return cls.objects.filter(
                tipo__exact=tipo,
                tipo_servico__exact=nome_tipo_servico,
                canal__exact=canal,
            )
        elif nome_campanha and nome_tipo_servico and tipo and canal and nome_produto == 'ALL':
            return cls.objects.filter(
                tipo__exact=tipo,
                tipo_servico__exact=nome_tipo_servico,
                canal__exact=canal,
                nome_campanha__exact=nome_campanha,
            )
        elif nome_campanha and nome_tipo_servico and tipo and canal and nome_produto != 'ALL':
            return cls.objects.filter(
                tipo__exact=tipo,
                tipo_servico__exact=nome_tipo_servico,
                canal__exact=canal,
                nome_campanha__exact=nome_campanha,
                nome_produto__exact=nome_produto,
            )    
        else:
            # Caso algum filtro seja None ou vazio, retorne um queryset vazio
            return cls.objects.none()
    
    def __str__(self):
        return chekin(
            {
                "nome_produto":self.nome_produto,
                "nome_campanha":self.nome_campanha
                }
            )
     


def custom_upload_to(instance, filename):
    ext = os.path.splitext(filename)[1]  # Obtém a extensão do arquivo
    form_value = f"{instance.data}'_'{instance.protocolo}'_'{instance.tipo}'_'{instance.nome_campanha}'_'{instance.tipo_servico}'_'{instance.nome_produto}'_'{instance.canal}'_'{instance.estabelecimento}"  # O valor vindo do campo 'title' no formulário
    new_name = f"{form_value.replace(' ', '_')}{ext}"  # Define o novo nome
    return f"{new_name}"



class upload_photo_chekin(models.Model):
    chekin_id = models.AutoField(primary_key=True)  # Define chekin_id como a chave primária
    data = models.DateField(db_column='data')
    protocolo =  models.CharField(db_column='protocolo')  
    tipo = models.CharField(db_column='tipo')
    nome_campanha = models.CharField(db_column='nome_campanha')
    tipo_servico = models.CharField(db_column='tipo_servico')
    nome_produto = models.CharField(db_column='nome_produto')
    canal = models.TextField(db_column='canal')
    estabelecimento = models.TextField(db_column='estabelecimento')
    img =  models.ImageField(upload_to=custom_upload_to)
      

    class Meta:
        db_table = '"br_addidas"."chekin"'  # Nome da tabela existente
        managed = False  # Impede que o Django gerencie a tabela



class model_db_estabelecimento(models.Model):
    id_estabelecimento = models.AutoField(primary_key=True)  # Define chekin_id como a chave primári
    nome_estabelecimento = models.CharField(db_column='nome_estabelecimento')
    cidade = models.CharField(db_column='cidade')
    uf = models.CharField(db_column='uf')
    chave_store = models.CharField(db_column='chave_store')

    class Meta:
        db_table = '"br_addidas"."estabelecimento"'  # Nome da tabela existente
        managed = False  # Impede que o Django gerencie a tabela
   


class model_db_cardapio(models.Model):
    id_material = models.AutoField(primary_key=True)
    peca = models.CharField(db_column='peca')
    variacao = models.CharField(db_column='variacao')
    Preco_uni = models.CharField(db_column='Preco uni')
    Preco_maior_10 = models.CharField(db_column='Preco > 10')
    Preco_maior_30 = models.CharField(db_column='Preco > 30')
    Preco_maior_50 = models.CharField(db_column='Preco > 50')

    class Meta:
        db_table = '"br_addidas"."cardapio_materiais"'  # Nome da tabela existente
        managed = False  # Impede que o Django gerencie a tabela



class model_db_plano_acao(models.Model):
    id_plano_acao = models.AutoField(primary_key=True)
    canal = models.CharField(db_column='canal')
    campanha = models.CharField(db_column='campanha')
    loja = models.CharField(db_column='loja')
    cidade = models.CharField(db_column='cidade')
    estado = models.CharField(db_column='estado')
    produto = models.CharField(db_column='produto')
    quantidade = models.CharField(db_column='quantidade')
    valor_unit = models.CharField(db_column='valor_unit')
    nome_arquivo = models.CharField(db_column='nome_arquivo')
    

    class Meta:
        db_table = '"br_addidas"."plano_acao"'  # Nome da tabela existente
        managed = False  # Impede que o Django gerencie a tabela

    def __str__(self):
        return self.nome


    



            
