from django import forms

class MathForm(forms.Form):
    input1 = forms.FloatField(label="Número 1")
    input2 = forms.FloatField(label="Número 2")
    OPERATION_CHOICES = [
        ('add', 'Sumar'),
        ('sub', 'Restar'),
        ('mul', 'Multiplicar'),
        ('div', 'Dividir'),
    ]
    operation = forms.ChoiceField(choices=OPERATION_CHOICES, label="Operación")
