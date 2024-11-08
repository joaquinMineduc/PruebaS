import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
# Configura el idioma a español (esto puede variar según el sistema operativo)
#locale.setlocale(locale.LC_TIME, 'es_ES.utf8')

# Funcion para transformar periodo
def transform(periodo):
    fecha = datetime(2024, periodo, 1)
    mes = fecha.strftime("%B")
    print(mes)

transform(1)
