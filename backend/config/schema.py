import graphene

import products.schema
import users.schema


class Query(products.schema.Query, users.schema.Query):
    pass


class Mutation(products.schema.Mutation, users.schema.Mutation):
    pass


schema = graphene.Schema(mutation=Mutation, query=Query)
