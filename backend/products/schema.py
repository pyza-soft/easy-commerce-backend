import graphene
from graphene_django import DjangoObjectType

from products.models import (
    Brand,
    Category,
)


class BrandType(DjangoObjectType):
    class Meta:
        model = Brand


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class BrandQuery(graphene.ObjectType):
    brands = graphene.List(BrandType)
    
    def resolve_brands(self, info):
        return Brand.objects.all()


class CategoryQuery(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    
    def resolve_categories(self, info):
        return Category.objects.all()


class CreateBrand(graphene.Mutation):
    brand = graphene.Field(BrandType)
    
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        image = graphene.ImageField()
    
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
        brand_id = graphene.Int()
        name = graphene.String()
        description = graphene.String()
    
    def mutate(self, info, **kwagrs):
        brand = Brand.objects.get(id=kwagrs.get('brand_id'))
        brand.name = kwagrs.get('name')
        brand.description = kwagrs.get('description')
        brand.image = info.context.FILES
        brand.save()
        
        return UpdateBrand(brand=brand)


class DeleteBrand(graphene.Mutation):
    brand_id = graphene.Int()
    
    class Arguments:
        brand_id = graphene.Int(required=True)
    
    def mutate(self, info, **kwagrs):
        brand_id = kwagrs.get('brand_id')
        brand = Brand.objects.get(id=brand_id)
        brand.delete()
        
        return DeleteBrand(brand_id=brand_id)


class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)
    
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        image = graphene.ImageField()
    
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
        category_id = graphene.Int()
        name = graphene.String()
        description = graphene.String()
    
    def mutate(self, info, **kwagrs):
        category = Category.objects.get(id=kwagrs.get('category_id'))
        category.name = kwagrs.get('name')
        category.description = kwagrs.get('description')
        category.image = info.context.FILES
        category.save()
        
        return UpdateCategory(category=category)


class DeleteCategory(graphene.Mutation):
    category_id = graphene.Int()
    
    class Arguments:
        category_id = graphene.Int(required=True)
    
    def mutate(self, info, **kwagrs):
        category_id = kwagrs.get('category_id')
        category = Category.objects.get(id=category_id)
        category.delete()
        
        return DeleteCategory(category_id=category_id)


class Mutation(graphene.ObjectType):
    create_brand = CreateBrand.Field()
    update_brand = UpdateBrand.Field()
    delete_brand = DeleteBrand.Field()
    
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()