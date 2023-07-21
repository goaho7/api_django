from django.urls import path
from api.views import generate, get_statement_by_id, get_statements_by_slang

urlpatterns = [
    path('v1/generate', generate),
    path('v1/statement/<int:id>', get_statement_by_id),
    path('v1/statements/<str:slang>', get_statements_by_slang),
]
