import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from .models import Publicacion, Capitulo, Articulo, Parrafo

class PublicacionType(DjangoObjectType):
    class Meta:
        model = Publicacion

class CapituloType(DjangoObjectType):
    class Meta:
        model = Capitulo

class ArticuloType(DjangoObjectType):
    class Meta:
        model = Articulo

class ParrafoType(DjangoObjectType):
    class Meta:
        model = Parrafo

class Query(graphene.ObjectType):
    publicaciones = graphene.List(PublicacionType)

    def resolve_publicaciones(self, info):
        return Publicacion.objects.all()

class CreatePublicacion(graphene.Mutation):
    publicacion = graphene.Field(PublicacionType)

    class Arguments:
        titulo = graphene.String()
        descripcion = graphene.String()

    def mutate(self, info, titulo, descripcion):
        publicacion = Publicacion(titulo=titulo, descripcion=descripcion)
        publicacion.save()

class CreateCapitulo(graphene.Mutation):
    capitulo = graphene.Field(CapituloType)

    class Arguments:
        titulo = graphene.String()
        orden = graphene.Int()

    def mutate(self, info, titulo, orden, publicacion_id):
        capitulo = Capitulo(titulo=titulo, orden=orden, publicacion_id=publicacion_id)
        capitulo.save()

class CreateArticulo(graphene.Mutation):
    articulo = graphene.Field(ArticuloType)

    class Arguments:
        titulo = graphene.String()
        orden = graphene.Int()

    def mutate(self, info, titulo, orden, capitulo_id):
        articulo = Articulo(titulo=titulo, orden=orden, capitulo_id=capitulo_id)
        articulo.save()

class CreateParrafo(graphene.Mutation):
    parrafo = graphene.Field(ParrafoType)

    class Arguments:
        texto = graphene.String()
        orden = graphene.Int()

    def mutate(self, info, texto, orden, articulo_id):
        parrafo = Articulo(texto=texto, orden=orden, articulo_id=articulo_id)
        parrafo.save()
class Mutation(graphene.ObjectType):
    create_publicacion = CreatePublicacion.Field()
    create_capitulo = CreateCapitulo.Field()
    create_articulo = CreateArticulo.Field()
    create_parrafo = CreateParrafo.Field()