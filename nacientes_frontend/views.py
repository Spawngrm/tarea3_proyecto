from django.shortcuts import render

# Create your views here.
def nacientesListaMapa(request):
    return render(request, 'nacientes_frontend/nacientes_base.html')
