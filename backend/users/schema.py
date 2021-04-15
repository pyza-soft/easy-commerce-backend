import graphene
import graphql_jwt

from .queries import UserQuery
from .mutations import ObtainJSONWebToken


class Query(UserQuery):
    pass


class Mutation(graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
