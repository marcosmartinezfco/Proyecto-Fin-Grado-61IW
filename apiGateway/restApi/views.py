from rest_framework.views import APIView
from django.http import JsonResponse
from restApi.client import Client
import json
import os


class PredictionView(APIView):
    """
    Class based view for all the nasdaq related requests
    """

    def get(self, request, ticker: str):
        client = Client(os.getenv('PIPELINE_IP', 'data-pipeline'), 15032)
        data = client.connect(ticker)
        return JsonResponse(json.loads(data))
