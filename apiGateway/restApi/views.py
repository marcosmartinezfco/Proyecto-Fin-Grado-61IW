from rest_framework.views import APIView
from django.http import JsonResponse
from restApi.client import Client
import json
import os
import requests
import pandas as pd


class PredictionView(APIView):
    """
    Class based view for all the nasdaq related requests
    """

    def get(self, request, ticker: str):
        client = Client(os.getenv('PIPELINE_IP', 'data-pipeline'), 15032)
        data = client.connect(ticker)
        raw_df = pd.DataFrame(json.loads(data)["Time Series (Daily)"]).T
        for c in raw_df.columns:
            raw_df[c] = pd.to_numeric(raw_df[c])
        raw_df.index = pd.to_datetime(raw_df.index)
        response = requests.post('http://172.18.0.3:8501/v1/models/mlp_model:predict', data=json.dumps({
            "signature_name": "serving_default",
            "instances":  raw_df.sort_index().iloc[-1].to_numpy().tolist()
        }))
        response.raise_for_status()
        return JsonResponse(response.json())
