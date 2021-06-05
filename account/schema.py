import graphene
from graphene_django import DjangoObjectType

from .models import Account


class AccountType(DjangoObjectType):
    class Meta:
        model = Account


class CreateAccount(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        username = graphene.String()

    account = graphene.Field(lambda: AccountType)

    def mutate(self, info, name, username):
        account = Account.objects.create(name=name, username=username)
        return CreateAccount(account=account)


class Query(graphene.ObjectType):
    accounts = graphene.List(AccountType)

    def resolve_accounts(self, info, **kwargs):
        return Account.objects.all()


class Mutation(graphene.ObjectType):
    create_account = CreateAccount.Field()
