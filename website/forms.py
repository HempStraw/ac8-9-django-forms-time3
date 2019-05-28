from django import forms
from django.core.mail import send_mail

class ContatoForm(forms.Form):
    ASSUNTOS =(
        ('B', 'Bug'),
        ('R', 'Reclamação'),
        ('S', 'Sugestão'),
    )   
    RESPOSTAS = (
        ('T', 'Telefone'),
        ('E', 'E-mail'),
    )
    nome = forms.CharField(
        min_length=3,
        max_length=120
    )
    email = forms.EmailField(
        required = False
    )
    telefone = forms.CharField(
        required = False
    )
    assunto = forms.ChoiceField(
        choices = ASSUNTOS
    )
    mensagem = forms.CharField()
    resposta = forms.MultipleChoiceField(
    required = False,
    choices=RESPOSTAS
    )

    def clean(self):
        dados = self.cleaned_data
        respostas = dados["resposta"]
        email = dados["email"]

        if "E" in respostas and email=="":
            self.add_error('email', 'e-mail é obrigatório se reposta for incluido')

    def enviar_email(self):
        pass