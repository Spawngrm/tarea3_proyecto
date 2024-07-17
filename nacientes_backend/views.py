from .models import Naciente
from .serializers import NacienteSerializador
from rest_framework import generics

# Create your views here.
class NacienteLista(generics.ListAPIView):
    queryset = Naciente.objects.all()
    serializer_class = NacienteSerializador
    name = 'naciente-lista'