import jwt

from django.http import JsonResponse
from django.conf import settings 

from .models import User

def login_authorization(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization')
            payload      = jwt.decode(access_token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
            request.user = User.objects.get(id = payload['id'])

            return func(self, request)
        except jwt.exceptions.DecodeError:
            return JsonResponse({"message":"TOKEN_ERROR"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message":"INVALID_ID"}, status=404)
    
    return wrapper