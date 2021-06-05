import graphene

import account.schema
import items.schema
import tweet.schema


class Query(
    tweet.schema.Query, account.schema.Query, items.schema.Query, graphene.ObjectType
):
    pass


class Mutation(
    tweet.schema.Mutation,
    account.schema.Mutation,
    items.schema.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,  # 追加
)
