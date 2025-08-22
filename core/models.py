from django.db import models
from stdimage.models import StdImageField

#_SIGNALS
from django.db.models import signals
from django.template.defaultfilters import  slugify


# Essa classe Base é uma classe abstrata, ou seja ela nao será criada no banco.
# Servirá somente para uso de outras classes

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado =models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
#################################################################################

class Produto(Base): # essa classe extendeu a Base.  Lembra que ela a base é abstrata
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124,124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=Produto)


# o signals serve para mandar um sinal.  No caso ele pede para sempre que rodar Produto
# sender=Produto ==> execute a função pproduto_pre_save.  Que por sua vez vai fazer o slug

# Sempre que criar um modelo tem que executar o migrations no consolte
#python manage.py makemigrations


