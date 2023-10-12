from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import redis
import json
from datetime import timedelta
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.core.cache import cache as redis
 

class GitHubSearchView(APIView):

    @swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'search_type': openapi.Schema(type=openapi.TYPE_STRING, description='Possible entries are users, repositories, or issues. Enter the search type you want to look for'),
            'search_text': openapi.Schema(type=openapi.TYPE_STRING, description='Type the text you want to search for that might be a usernmae of a repositry name in github'),
        },
        
    ),
)
    def post(self, request):
        search_type = request.data.get('search_type')
        search_text = request.data.get('search_text')

        # Check if the result is cached
        cache_key = f"{search_type}_{search_text}"
        cached_result = redis.get(cache_key)
        
        if cached_result:
            return Response(json.loads(cached_result), status=status.HTTP_200_OK)

        # If not cached, fetch data from GitHub API
        github_url = f"https://api.github.com/search/{search_type}?q={search_text}"
        response = requests.get(github_url)

        if response.status_code == 200:
            result_data = response.json()
            # Cache the result for 2 hours
            redis.set(cache_key,json.dumps(result_data),7200)
            return Response(result_data, status=status.HTTP_200_OK)
        else:
            return Response(response.json(), status=response.status_code)

class ClearCacheView(APIView):
    def post(self, request):

        redis.clear()  # Clear the entire Redis cache
        
        return Response({'message': 'Cache cleared successfully'}, status=status.HTTP_200_OK)
