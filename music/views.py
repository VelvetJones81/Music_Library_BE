from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MusicSerializer
from .models import Music
from music import serializers

@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        music = Music.objects.all()
        serializer = MusicSerializer(music, many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data, status= status.HTTP_201_CREATED)
    
  
    return Response(serializer.data)


@api_view(['GET', 'PUT','DELETE'])
def music_details(request, pk):
    music = get_object_or_404 (Music, pk=pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save
        return Response(serializer.data)
    elif request.method == 'DELETE':
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
