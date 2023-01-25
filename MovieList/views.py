from rest_framework.response import Response
from MovieList.serializers import MovieSerializer
from MovieList.models import Movie
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])
def showMovie(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET'])
def MovieDetails(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
