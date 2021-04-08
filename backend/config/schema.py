import graphene
import graphql_jwt
import products.schema

class Query(products.schema.BrandQuery, products.schema.CategoryQuery, graphene.ObjectType):
    title = graphene.String(default_value="Easy Commerce!")


class Mutation(products.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(mutation=Mutation, query=Query)
