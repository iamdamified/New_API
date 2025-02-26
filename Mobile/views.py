from django.shortcuts import render
from Blog.models import Post
from .serializers import PostSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions, authentication
# Create your views here.
# authentication_classes = []  # Disable CSRF for testing (remove in production)
# permission_classes = [permissions.AllowAny]

@api_view(["GET"])
def mobile_home(request):
    all_posts = Post.objects.all()
    serialized_data = PostSerializers(all_posts, many=True)
    return Response(serialized_data.data)


@api_view(["GET"])
def mobile_post_detail(request, id):
    post_detail = Post.objects.get(id=id)
    serialized_detail = PostSerializers(post_detail)
    return Response(serialized_detail.data)

@api_view(["PUT"])
def mobile_post_update(request, id):
    post_detail = Post.objects.get(id=id)
    update_data = request.data
    serialized_update = PostSerializers(post_detail, data=update_data, partial=True)
    if serialized_update.is_valid():
        serialized_update.save()
        return Response(serialized_update.data)
    else:
        return Response({"Error": "You entered the wrong data"})
    

@api_view(["DELETE"])
def mobile_post_delete(request, id):
    post_detail = Post.objects.get(id=id) # A query set
    post_detail.delete() #delete
    return Response({"Success": "Post has been successfully deleted"})

@csrf_exempt
@api_view(["POST"])
def mobile_post_create(request):
    new_data = PostSerializers(data=request.data)
    if new_data.is_valid():
        new_data.save()
        return Response({'message': 'Data created!'}, status=status.HTTP_201_CREATED)
        # return Response(new_data.data)