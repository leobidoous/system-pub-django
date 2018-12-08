from rest_framework import viewsets
from webservice.models import PessoaModel
from webservice.serializers import PessoaSerializer

# Create your views here.
class PessoasViewSet(viewsets.ModelViewSet):
    queryset = PessoaModel.objects.all()
    serializer_class = PessoaSerializer