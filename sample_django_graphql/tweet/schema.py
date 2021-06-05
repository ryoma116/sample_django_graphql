import graphene
from graphene_django import DjangoObjectType

from .models import Tweet


class TweetType(DjangoObjectType):
    class Meta:
        model = Tweet


class CreateTweet(graphene.Mutation):
    class Arguments:
        text = graphene.String()
        account_id = graphene.Int()

    tweet = graphene.Field(lambda: TweetType)

    def mutate(self, info, text, account_id):
        tweet = Tweet.objects.create(text=text, account_id=account_id)
        return CreateTweet(tweet=tweet)


class Query(graphene.ObjectType):
    tweet = graphene.Field(TweetType, id=graphene.Int(), account_id=graphene.Int())
    tweets = graphene.List(TweetType, account_id=graphene.Int())

    def resolve_tweet(self, info, id=None):
        if id:
            return Tweet.objects.get(pk=id)

        return Tweet.objects.all()

    def resolve_tweets(self, info, account_id=None):
        if account_id:
            return Tweet.objects.filter(account__id=account_id)

        return Tweet.objects.all()


class Mutation(graphene.ObjectType):
    create_tweet = CreateTweet.Field()
