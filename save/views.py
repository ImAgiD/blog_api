# from django.shortcuts import render

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from django.shortcuts import get_object_or_404

# from .serializers import SaveSerializer
# from posts.views import Post
# from .models import SavedPost

# class SaveAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = SaveSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     @api_view(['POST'])
#     def toggle_favorites(request, id):
#         user = request.user
#         if not user.is_authenticated:
#             return Response(status=401)
#         post = get_object_or_404(SavedPost, id=id)
#         if SavedPost.objects.filter(user=user, post=post).exists():
#             SavedPost.objects.filter(user=user, post=post).delete()        
#         else:
#             SavedPost.objects.create(user=user, post=post)
#         return Response(201) 