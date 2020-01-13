from .models import Publicacion, Capitulo, Articulo, Parrafo

def initialize():
    constitucion = Publicacion(titulo="Constitucion Politica de Chile", descripcion="Descripcion politica de Chile")
    constitucion.save()

    capitulo1 = Capitulo(titulo="Capitulo 1: Bases de la institucionalidad", orden=1, constitucion=constitucion)
    capitulo1.save()

    articulo1 = Articulo(titulo="Articulo 1", orden=1, capitulo = capitulo1)
    articulo1.save()

    parrafo1 = Parrafo(texto="Las personas nacen libres e iguales en dignidad y derechos.", orden=1, articulo=articulo1)
    parrafo1.save()
    parrafo2 = Parrafo(texto="La familia es el núcleo fundamental de la sociedad.", orden=2, articulo=articulo1)
    parrafo2.save()
    parrafo3 = Parrafo(texto="El Estado reconoce y ampara a los grupos intermedios a través de los cuales se organiza y estructura la sociedad y les garantiza la adecuada autonomía para cumplir sus propios fines específicos.", orden=3, articulo=articulo1)
    parrafo3.save()

    