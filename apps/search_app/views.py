from rest_framework.response import Response
from rest_framework.decorators import api_view
from services.db_embd_service import query


@api_view(['GET'])
def getData(request):
    user_query = request.query_params.get('query')
    resp = query(user_query)
    return Response(resp)
