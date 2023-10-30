from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, UserProfile
from .serializers import *
from .util import *

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def users_list(request):
    if request.method == 'GET':
        if 'username' in request.GET:
            users = UserProfile.objects.filter(username=request.GET.get('username'))
        elif 'email' in request.GET:
            users = User.objects.filter(email=request.GET.get('email'))
            users = [user.profile for user in users]
        else:
            users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
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

@api_view(['PUT', 'DELETE'])
def users_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
          
