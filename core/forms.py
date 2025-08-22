from django import forms
from django.core.mail.message import EmailMessage

from .models import Produto # Importando o model Produto para usar no form

#Essa classe herda Form, que é usada mais para formulario, diferente da de baixo que é usada para banco
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome',max_length=100, min_length=5)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\n Email: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br',],
            headers={'Reply-to': email}
        )
        mail.send()

#aqui herdamos a classe MoodelForm, pq tem comportamento diferente.  Será usada para banco.
class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','estoque','imagem']