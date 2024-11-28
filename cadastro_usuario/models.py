from django.db import models

class CheckinI(models.Model):
    
    chekin_id = models.AutoField(primary_key=True)  # Define chekin_id como a chave primária

    estabelecimento = models.TextField(db_column='estabelecimento')
    img =  models.TextField(db_column='img')
    cidade = models.TextField(db_column='cidade')
    estado = models.TextField(db_column='estado')
    tipo = models.TextField(db_column='tipo')
    fk_campanha = models.IntegerField(db_column='fk_campanha')
    nome_produto = models.TextField(db_column='nome_produto')

    class Meta:
        db_table = '"br_addidas"."chekin"'  # Nome da tabela existente
        managed = False  # Impede que o Django gerencie a tabela


    @classmethod
    def get_by_instalacao(cls,nome_tipo, fk_campanha,nome_produto):
        # Verifique se ambos os filtros têm valores antes de realizar a consulta
        if fk_campanha and nome_tipo:
            return cls.objects.using('default').filter(
                fk_campanha__icontains=fk_campanha,
                nome_produto__icontains=nome_produto,
                tipo__icontains=nome_tipo,
            )
        else:
            # Caso algum filtro seja None ou vazio, retorne um queryset vazio
            return cls.objects.none()
    
    def __str__(self):
        return self.nome_produto
     
        

class model_db_campanha(models.Model):

    id_campanha = models.AutoField(primary_key=True)
    nome_campanha = models.CharField(db_column='nome_campanha')
    tipo = models.CharField(db_column='tipo')

    class Meta:
        db_table = '"br_addidas"."campanha"'  # Nome da tabela existente
        managed = False  # Impede que o Django gerencie a tabela
    
    @classmethod
    def get_by_campanha(cls,tipo):
        # Verifique se ambos os filtros têm valores antes de realizar a consulta
        if tipo:
            return cls.objects.using('default').filter(
                tipo__icontains=tipo,
            )
        else:
            # Caso algum filtro seja None ou vazio, retorne um queryset vazio
            return cls.objects.none()

    def __str__(self):
        return self.nome_campanha

       
class model_db_projeto(models.Model):
    id_projeto = models.AutoField(primary_key=True)
    nome_projeto = models.CharField(db_column='nome_projeto')
    canal = models.CharField(db_column='canal')

    class Meta:
        db_table = '"br_addidas"."projeto"'  # Nome da tabela existente
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




    



            
