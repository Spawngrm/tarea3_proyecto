from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Naciente

nacientes_mapping = {
    'wkt': 'WKT',
    'sistema_de': 'SISTEMA_DE',
    'punto_de_m': 'PUNTO_DE_M',
    'n': 'N',
    'e': 'E',
    'nitrato': 'Nitrato',
    'distrito': 'Distrito',
    'canton': 'Canton',
    'provincia': 'Provincia',
    'r_cont_n': 'r_cont_n',
    'c_canton': 'c_canton',
    'point_x': 'POINT_X',
    'point_y': 'POINT_Y',
    'id_n': 'id_n',
    'c_distrito': 'c_distrito',
    'geom': 'POINT',
}

nacientes_gpkg = Path(__file__).resolve().parent / 'datos' / 'nacientes.gpkg'

def run(verbose=True):
    lm = LayerMapping(Naciente, nacientes_gpkg, nacientes_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)