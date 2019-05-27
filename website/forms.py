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
        min_length = 3,
        max_length = 120
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
    resposta = forms.MutipleChoiceField(
        required = False
        choices = RESPOSTAS
    )


    def enviar_email(self):
        pass