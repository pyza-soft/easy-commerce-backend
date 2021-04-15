import graphene

from .queries import BrandQuery, CategoryQuery
from .mutations import (
    CreateBrand,
    UpdateBrand,
    DeleteBrand,
    CreateCategory,
    UpdateCategory,
    DeleteCategory,
)


class Query(BrandQuery, CategoryQuery):
    pass


class Mutation(graphene.ObjectType):
    create_brand = CreateBrand.Field()
    update_brand = UpdateBrand.Field()
    delete_brand = DeleteBrand.Field()

    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
