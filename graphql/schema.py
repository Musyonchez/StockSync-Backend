# graphql/schema.py

import graphene
from graphene_django.debug import DjangoDebug
from .types import Query as App1Query
from .types import Mutation as App1Mutation

class Query(App1Query, graphene.ObjectType):
    # Add queries from other apps if any
    debug = graphene.Field(DjangoDebug, name='__debug')

class Mutation(App1Mutation, graphene.ObjectType):
    # Add mutations from other apps if any
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
