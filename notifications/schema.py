# app1/schema.py

import graphene
from graphene_django.types import DjangoObjectType
from .models import YourModel

class YourModelType(DjangoObjectType):
    class Meta:
        model = YourModel

class Query(graphene.ObjectType):
    # Define query fields here
    all_your_models = graphene.List(YourModelType)

    def resolve_all_your_models(self, info):
        # Return all instances of YourModel
        return YourModel.objects.all()

class Mutation(graphene.ObjectType):
    # Define mutation fields here
    create_your_model = CreateYourModel.Field()
    update_your_model = UpdateYourModel.Field()
    delete_your_model = DeleteYourModel.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
