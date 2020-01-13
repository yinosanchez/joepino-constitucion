import graphene
import publicacion.schema
import graphql_jwt

class Query(publicacion.schema.Query, graphene.ObjectType):
    pass

class Mutation(publicacion.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)