from graphene_django import DjangoObjectType

from .models import Brand, Category


class BrandType(DjangoObjectType):
    class Meta:
        model = Brand


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
