import json, bcrypt, jwt 

from django.conf  import settings
from django.forms import ValidationError

from django.http  import JsonResponse
from django.views import View

from .models    import User
from .validator import validate_signup
from .utils     import login_decorator

class SignUpView(View):
    def post(self, request):
        try: 
            data = json.loads(request.body)
            user         = data['user']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']

            validate_signup(email,password)

            if User.objects.get(email=email):
                return JsonResponse({'message':'ID_ALREADY_EXISTS'}, status=401)
            
            hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
            User.objects.create(
                user         = user,
                email        = email,
                password     = hashed_password,
                phone_number = phone_number
            )
            return JsonResponse({'message':'ACCOUNT_CREATED'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
  
class SignInView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user     = User.objects.get(email=email)
            email    = data['email']
            password = data['password']

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message':'INVALID_PASSWORD'}, status=401)
            
            access_token = jwt.encode({'id':user.id}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
            return JsonResponse({'token':access_token}, status=200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_ID'}, status=404)
        except ValidationError as e:
            return JsonResponse({'message':e.message}, status=401)