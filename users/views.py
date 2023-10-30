from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, UserProfile
from .serializers import *
from .util import *


class UsersList(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, format=None):
        if 'username' in request.GET:
            users = UserProfile.objects.filter(username=request.GET.get('username'))
        elif 'email' in request.GET:
            users = User.objects.filter(email=request.GET.get('email'))
            users = [user.profile for user in users]
        else:
            users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, context={'request': request}, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        user_serializer = UserSerializer(data=request.data)
        new_user = None
        if user_serializer.is_valid():
            new_user = user_serializer.save()
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        profile_serializer = UserProfileSerializer(data={'user': new_user.id, 'username': request.data.get('username')})
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response({'message': 'User and profile created successfully.'}, status=status.HTTP_201_CREATED)
        else:
            new_user.delete()
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Following(APIView):
    permission_classes = (IsAuthenticated, )
    def put(self, request, target_id, format=None):
        if request.user.id != target_id:
            try:
                user = User.objects.get(pk=request.user.id)
                target_user = User.objects.get(pk=target_id)

                user.profile.following.add(target_user.profile)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                print(e)
                return Response(e, status=status.HTTP_400_BAD_REQUEST)
        else:
            print('Can\'t follow yourself.')
            return Response('Can\'t follow yourself.', status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
          
