from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, Profile
from .serializers import *
from .util import *


class UserList(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, context={'request': request}, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        user_serializer = UserSerializer(data=request.data)
        new_user = None
        if user_serializer.is_valid():
            new_user = user_serializer.save()
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        profile_serializer = ProfileSerializer(data={'user': new_user.id})
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response({'message': 'User and profile created successfully.'}, status=status.HTTP_201_CREATED)
        else:
            new_user.delete()
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UserDetail(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, identifier, format=None):
        try:
            if identifier.isdigit():
                user = User.objects.get(id=int(identifier))
            else:
                user = User.objects.get(username=identifier)
            serializer = UserSerializer(user, context={'request': request})

            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class FollowerList(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, identifier, format=None):
        try:
            if identifier.isdigit():
                user = User.objects.get(id=int(identifier))
            else:
                user = User.objects.get(username=identifier)
            followers = user.followers.all()
            followers_serializer = UserSerializer(followers, context={'request': request}, many=True)

            return Response(followers_serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class FollowView(APIView):
    permission_classes = (IsAuthenticated, )
    def put(self, request, identifier, format=None):
        try:
            if identifier.isdigit():
                target_user = User.objects.get(id=int(identifier))
            else:
                target_user = User.objects.get(username=identifier)
            user = User.objects.get(pk=request.user.id)
            if user.id == target_user.id:
                return Response('Can\'t follow yourself.', status=status.HTTP_400_BAD_REQUEST)

            user.following.add(target_user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
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
          
