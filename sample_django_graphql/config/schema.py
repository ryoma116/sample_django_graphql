import account.schema
import graphene
import tweet.schema


class Query(tweet.schema.Query, account.schema.Query, graphene.ObjectType):
    pass


class Mutation(
    tweet.schema.Mutation,
    account.schema.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,  # 追加
)
