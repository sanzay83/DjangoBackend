from DjangoBackend.models import Items, Posts
from DjangoBackend.serializers import ItemsSerializer, PostsSerializer
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

@api_view(['POST'])
def reg_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            User.objects.create(
                username=username,
                password=make_password(password),
                
            )
            return Response({"message": "Admin user created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        if not user.is_active:
            return Response({"error": "User account is disabled"}, status=status.HTTP_403_FORBIDDEN)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id,
            'username': user.username
        }, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

########################################################################
################    API FOR TIMELESS TRENDS       ######################
########################################################################
@api_view(['GET','POST','DELETE'])
def itemsApi(request, id=0):
  if request.method=='GET':
    item = Items.objects.all()
    item_serializer = ItemsSerializer(item, many=True)
    return JsonResponse(item_serializer.data, safe=False)
  elif request.method=='POST':
    item_data = JSONParser().parse(request)
    item_serializer = ItemsSerializer(data=item_data)
    if item_serializer.is_valid():
      item_serializer.save()
      return Response({"message": "Added successfully"}, status=status.HTTP_201_CREATED)
    return Response({"error": "Failed to add"}, status=status.HTTP_400_BAD_REQUEST)
  elif request.method=='DELETE':
    item =Items.objects.get(item_id=id)
    item.delete()
    return JsonResponse("Deleted Successfully", safe=False)
  
########################################################################
###############     API FOR VENT IT OUT           ######################
########################################################################
@api_view(['GET','POST','DELETE'])
def vio_posts(request, id=0):
  if request.method=='GET':
    post = Posts.objects.all()
    post_serializer = PostsSerializer(post, many=True)
    return JsonResponse(post_serializer.data, safe=False)
  elif request.method=='POST':
    post_data = JSONParser().parse(request)
    post_serializer = PostsSerializer(data=post_data)
    if post_serializer.is_valid():
      post_serializer.save()
      return Response({"message": "Added successfully"}, status=status.HTTP_201_CREATED)
    return Response({"error": "Failed to add"}, status=status.HTTP_400_BAD_REQUEST)
  elif request.method=='DELETE':
    post =Posts.objects.get(post_id=id)
    post.delete()
    return JsonResponse("Deleted Successfully", safe=False)