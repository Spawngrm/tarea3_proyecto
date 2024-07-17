from .models import Naciente
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class NacienteSerializador(GeoFeatureModelSerializer):
    class Meta:
        model = Naciente
        geo_field = 'geom'

        fields = (
            'id',
            'wkt',
            'sistema_de',
            'punto_de_m',
            'n',
            'e',
            'nitrato',
            'distrito',
            'canton',
            'r_cont_n',
            'c_canton',
            'point_x',
            'point_y',
            'c_distrito'
        )