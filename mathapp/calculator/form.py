from django import forms

class MathForm(forms.Form):
    input1 = forms.FloatField(label="Number 1")
    input2 = forms.FloatField(label="Number 2")
    OPERATION_CHOICES = [
        ('add', 'add'),
        ('sub', 'subtract'),
        ('mul', 'Multiply'),
        ('div', 'Divide'),
    ]
    operation = forms.ChoiceField(choices=OPERATION_CHOICES, label="Operación")