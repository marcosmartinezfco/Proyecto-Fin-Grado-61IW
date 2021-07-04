from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status


class PredictionView(APIView):
    """
    Class based view for all the nasdaq related requests
    """

    def get(self, request, ticker: str):
        return JsonResponse({'ticker': ticker})
