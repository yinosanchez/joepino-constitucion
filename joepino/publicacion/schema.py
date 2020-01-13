import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from .models import Publicacion, Capitulo, Parrafo

class PublicacionType(DjangoObjectType):
    class Meta:
        model = Publicacion

class CapituloType(DjangoObjectType):
    class Meta:
        model = Capitulo

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
        orden = graphene.Integer()

    def mutate(self, info, titulo, orden, publicacion_id):
        capitulo = Capitulo(titulo=titulo, orden=orden, publicacion_id=publicacion_id)
        capitulo.save()

class Mutation(graphene.ObjectType):
    create_publicacion = CreatePublicacion.Field()
    create_capitulo = CreateCapitulo.Field()