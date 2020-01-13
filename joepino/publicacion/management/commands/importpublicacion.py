from django.core.management.base import BaseCommand, CommandError
from publicacion.models import Publicacion,Capitulo,Articulo,Parrafo

class Command(BaseCommand):
    help = 'Importa una publicacion desde un archivo de texto plano'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str)

    def handle(self, *args, **options):
        for document_file in options['file']:
            with open(document_file, 'r', encoding="utf-8") as df:
                publicacion = None
                last_capitulo = None
                last_articulo = None
                orden_capitulo = 0
                orden_articulo = 0
                orden_parrafo = 0
                line = df.readline()
                while line:
                    #stuff
                    if publicacion is None:
                        titulo = line
                        descripcion = df.readline()
                        publicacion = Publicacion(titulo=titulo, descripcion=descripcion)
                        publicacion.save()
                    else:
                        first_word = line.split(' ',1)[0]
                        if first_word == 'Capítulo' or first_word == 'Capitulo':
                            orden_parrafo = 0
                            last_capitulo = Capitulo(titulo=line, orden=orden_capitulo, publicacion_id=publicacion.id)
                            last_capitulo.save()
                            orden_capitulo = orden_capitulo+1
                        else:
                            if first_word == 'Articulo' or first_word == 'Artículo':
                                orden_parrafo = 0
                                last_articulo = Articulo(titulo=line, orden=orden_articulo, capitulo_id=last_capitulo.id)
                                last_articulo.save()
                                orden_articulo = orden_articulo+1
                            else:
                                parrafo = Parrafo(texto=line, orden=orden_parrafo, articulo_id=last_articulo.id)
                                parrafo.save()
                                orden_parrafo = orden_parrafo+1
                    line = df.readline()