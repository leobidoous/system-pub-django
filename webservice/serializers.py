from rest_framework import serializers
from webservice.models import PessoaModel

# Serializers define the API representation.
class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaModel
        fields = ('__all__')