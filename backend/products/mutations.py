import graphene
from graphql_jwt.decorators import login_required

from .models import Brand, Category
from .types import BrandType, CategoryType


class CreateBrand(graphene.Mutation):
    brand = graphene.Field(BrandType)

    class Arguments:
        name = graphene.String()
        description = graphene.String()
        image = graphene.String()

    @login_required
    def mutate(self, info, **kwagrs):
        brand = Brand(
            name=kwagrs.get('name'),
            description=kwagrs.get('description'),
            image=info.context.FILES
        )
        brand.save()
        return CreateBrand(brand=brand)


class UpdateBrand(graphene.Mutation):
    brand = graphene.Field(BrandType)

    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        description = graphene.String()
        image = graphene.String()

    @login_required
    def mutate(self, info, **kwagrs):
        brand = Brand.objects.get(id=kwagrs.get('id'))
        brand.name = kwagrs.get('name')
        brand.description = kwagrs.get('description')
        brand.image = info.context.FILES
        brand.save()

        return UpdateBrand(brand=brand)


class DeleteBrand(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.Int(required=True)

    @login_required
    def mutate(self, info, **kwagrs):
        brand_id = kwagrs.get('id')
        brand = Brand.objects.get(id=brand_id)
        brand.delete()
        return DeleteBrand(success=True)


class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        name = graphene.String()
        description = graphene.String()
        image = graphene.String()

    @login_required
    def mutate(self, info, **kwagrs):
        category = Category(
            name=kwagrs.get('name'),
            description=kwagrs.get('description'),
            image=info.context.FILES,
        )
        category.save()
        return CreateCategory(category=category)


class UpdateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        description = graphene.String()
        image = graphene.String()

    @login_required
    def mutate(self, info, **kwagrs):
        category = Category.objects.get(id=kwagrs.get('id'))
        category.name = kwagrs.get('name')
        category.description = kwagrs.get('description')
        category.image = info.context.FILES
        category.save()

        return UpdateCategory(category=category)


class DeleteCategory(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.Int(required=True)

    @login_required
    def mutate(self, info, **kwagrs):
        category_id = kwagrs.get('id')
        category = Category.objects.get(id=category_id)
        category.delete()
        return DeleteCategory(success=True)
