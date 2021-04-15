import graphene
from graphql_jwt.decorators import login_required

from .models import Brand, Category
from .types import BrandType, CategoryType


class BrandQuery(graphene.ObjectType):
    brands = graphene.List(BrandType)

    @login_required
    def resolve_brands(self, info):
        return Brand.objects.all()


class CategoryQuery(graphene.ObjectType):
    categories = graphene.List(CategoryType)

    @login_required
    def resolve_categories(self, info):
        return Category.objects.all()
