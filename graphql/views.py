# graphql/views.py

from django.http import JsonResponse
from graphene_django.views import GraphQLView

class CustomGraphQLView(GraphQLView):
    def execute_graphql_request(self, request, data, query, variables, operation_name, show_graphiql):
        # Implement custom logic here if needed
        return super().execute_graphql_request(request, data, query, variables, operation_name, show_graphiql)

graphql_view = CustomGraphQLView.as_view(graphiql=True)
