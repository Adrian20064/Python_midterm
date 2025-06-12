from django.shortcuts import render
from .form import MathForm


# Create your views here.

def calculate_view(request):
    result = None
    error = None

    if request.method == 'POST':
        form = MathForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['input1']
            b = form.cleaned_data['input2']
            op = form.cleaned_data['operation']

            try:
                if op == 'add':
                    result = a + b
                elif op == 'sub':
                    result = a - b
                elif op == 'mul':
                    result = a * b
                elif op == 'div':
                    if b != 0:
                        result = a / b
                    else:
                        error = "Error: División por cero"
                
                if result is not None:
                    if result > 100:
                        result *= 2
                    elif result < 0:
                        result += 50

            except Exception as e:
                error = str(e)
    else:
        form = MathForm()

    if result is not None or error:
        return render(request, 'calculator/result.html', {'result': result, 'error': error})
    return render(request, 'calculator/math_form.html', {'form': form})