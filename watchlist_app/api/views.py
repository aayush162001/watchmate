from rest_framework.response import Response
from watchlist_app.models import WatchList,StreamPlatform,Review
from watchlist_app.api.serializers import WatchSerilizer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import mixins,generics  
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from rest_framework .views import APIView


# Create your views here.
class ReviewCreate(generics.CreateAPIView):
    
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        
        serializer.save(watchlist=movie)


class ReviewList(generics.ListAPIView):

    serializer_class = ReviewSerializer 
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


# class ReviewList(generics.ListCreateAPIView):
    # serializer_class = ReviewSerializer
    
    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all() 
    serializer_class = ReviewSerializer


# class ReviewList(mixins.ListModelMixin,  mixins.CreateModelMixin, generics.GenericAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
class StreamPlatfromVS(viewsets.ViewSet):
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(watchlist)
        return Response(serializer.data)

class StreamPlatformAV(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True,context={'request':request})
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