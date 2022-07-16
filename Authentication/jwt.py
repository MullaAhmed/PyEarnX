from rest_framework.authentication import get_authorization_header,BasicAuthentication
from rest_framework import exceptions
import jwt
from django.conf import settings
from Authentication.models import User

class JWTAuthentication(BasicAuthentication):
    def authenticate(self, request):

        auth_header=get_authorization_header(request)
        auth_data=auth_header.decode('utf-8')
        auth_token=auth_data.split(" ")

        if len(auth_token)!=2:
            raise exceptions.AuthenticationFailed("Token not valid")
        
        token=auth_token[1]

        try:
            payload=jwt.decode(token,settings.SECRET_KEY,algorithms="HS256")
            
            wallet_address= payload['wallet_address']

            user=User.objects.get(wallet_address=wallet_address)

            return(user,token)

        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed("Token is expired, login again")
        
        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed("Token is invalid")

        except User.DoesNotExist as no_user:
             raise exceptions.AuthenticationFailed("User Not Found")

        return super().authenticate(request)

