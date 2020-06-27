import graphene
from graphene_django import DjangoObjectType
from articles.models import Article

class UserType(DjangoObjectType):
    class Meta:
        model = Article
class Query(graphene.ObjectType):
    Article = graphene.List(UserType)

    def resolve_Article(self, info):
        return Article.objects.all()

schema = graphene.Schema(query=Query)


