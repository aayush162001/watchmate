from rest_framework.response import Response
from watchlist_app.models import WatchList,StreamPlatform
from watchlist_app.api.serializers import WatchSerilizer,StreamPlatformSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework .views import APIView


# Create your views here.

class StreamPlatformAV(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class WatchListAV(APIView):
    
    def get(self,request):
        watch = WatchList.objects.all()
        serializer = WatchSerilizer(watch, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = WatchSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)        
        
class WatchDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            watch = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error':'Not Found'}, status= status.HTTP_404_NOT_FOUND )
        serializer = WatchSerilizer(watch)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        watch = WatchList.objects.get(pk=pk)
        serializer = WatchSerilizer(watch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        watch = WatchList.objects.get(pk=pk)
        watch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

# class MovieListAV(APIView):
    
#     def get(self,request):
#         movies = Movie.objects.all()
#         serializer = MoiveSerilizer(movies, many=True)
#         return Response(serializer.data , status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = MoiveSerilizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)        
        
# class MovieDetailAV(APIView):
    
    # def get(self, request,pk):
    #     try:
    #         movie = Movie.objects.get(pk=pk)
    #     except Movie.DoesNotExist:
    #         return Response({'Error':'Movie not Found'}, status= status.HTTP_404_NOT_FOUND )
    #     serializer = MoiveSerilizer(movie)
    #     return Response(serializer.data , status=status.HTTP_200_OK)
    
    # def put(self, request,pk):
    #     movie = Movie.objects.get(pk=pk)
    #     serializer = MoiveSerilizer(movie, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request,pk):
    #     movie = Movie.objects.get(pk=pk)
    #     movie.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
        
# @api_view(['GET','POST'])
# def movie_list(request):
    
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MoiveSerilizer(movies, many=True)
#         return Response(serializer.data , status=status.HTTP_200_OK)

#     if request.method == 'POST':
#         serializer = MoiveSerilizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)

    
    
# @api_view(['GET','PUT', 'DELETE'])
# def movie_details(request,pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not Found'}, status= status.HTTP_404_NOT_FOUND )
#         serializer = MoiveSerilizer(movie)
#         return Response(serializer.data , status=status.HTTP_200_OK)

#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MoiveSerilizer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)