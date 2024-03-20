# app1/mutations.py

import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from .models import YourModel
from .forms import YourModelForm

class YourModelFormMutation(DjangoModelFormMutation):
    class Meta:
        form_class = YourModelForm

class CreateYourModel(YourModelFormMutation):
    class Meta:
        form_class = YourModelForm

class UpdateYourModel(YourModelFormMutation):
    class Meta:
        form_class = YourModelForm

class DeleteYourModel(graphene.Mutation):
    # Define mutation logic here

class Mutation(graphene.ObjectType):
    create_your_model = CreateYourModel.Field()
    update_your_model = UpdateYourModel.Field()
    delete_your_model = DeleteYourModel.Field()
