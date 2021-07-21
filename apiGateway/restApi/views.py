from rest_framework.views import APIView
from django.http import JsonResponse
from restApi.client import Client
import json


class PredictionView(APIView):
    """
    Class based view for all the nasdaq related requests
    """

    def get(self, request, ticker: str):
        client = Client('127.0.1.1', 15032)
        data = client.connect(ticker)
        return JsonResponse(json.loads(data))
