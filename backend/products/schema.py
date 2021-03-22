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
        brand = Brand(
            name=kwagrs.get('name'),
            description=kwagrs.get('description'),
            image=info.context.FILES,
        )
        brand.save()
        
        return CreateBrand(brand)


class Mutation(graphene.ObjectType):
    create_brand = CreateBrand.Field()
    update_brand = UpdateBrand.Field()
    delete_brand = DeleteBrand.Field()