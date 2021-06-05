import graphene
from graphene_django import DjangoObjectType

from .models import Items


class Item(DjangoObjectType):
    class Meta:
        model = Items


class CreateItem(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        count = graphene.Int()

    item = graphene.Field(lambda: Item)

    def mutate(self, info, name, count):
        item = Items.objects.create(name=name, count=count)
        return CreateItem(item=item)


class Query(graphene.ObjectType):
    items = graphene.List(Item)

    def resolve_items(self, info, **kwargs):
        return Items.objects.all()


class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()
