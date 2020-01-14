from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models
from profiles_api import permissions


class HelloAPIView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello msg"""
        a_viewset = [
            'uses actions (list, create, retrieve, update, partial update)',
            'automatically maps to URLs using Routers',
            'provide more func with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """updating an object"""
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Partial update of an object"""
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """remove of an object"""
        return Response({'method': 'Delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """creating and updating user profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
