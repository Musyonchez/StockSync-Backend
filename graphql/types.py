# graphql/types.py

import graphene
from app1.models import YourModel1
from app2.models import YourModel2

class YourModel1Type(graphene.ObjectType):
    class Meta:
        model = YourModel1

class YourModel2Type(graphene.ObjectType):
    class Meta:
        model = YourModel2

class Query(graphene.ObjectType):
    # Define query fields here
    all_your_model1 = graphene.List(YourModel1Type)
    all_your_model2 = graphene.List(YourModel2Type)

    def resolve_all_your_model1(self, info):
        # Return all instances of YourModel1
        return YourModel1.objects.all()

    def resolve_all_your_model2(self, info):
        # Return all instances of YourModel2
        return YourModel2.objects.all()

class Mutation(graphene.ObjectType):
    # Define mutation fields here
    pass
