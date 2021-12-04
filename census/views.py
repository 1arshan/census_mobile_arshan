from . models import  State,District,Child,File
from .serializers import StateSerializer,DistrictSerializer,ChildSerializer,FileSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import time


class StateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    # queryset = State.objects.all()
    serializer_class = StateSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            data = serializer.save()
            x = {"success": "true",
            "status": 200,
            "message": "Operation performed successfully"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StateGetView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        state=State.objects.all()
        serializer=StateSerializer(state,many=True)
        x={"success": "true",
        "status": 200,
        "message": "State Detail",
        "timestamp": time.time(),
        "state":serializer.data}
        return Response(x)


class DistrictView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DistrictSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            data = serializer.save()
            x = {"success": "true",
            "status": 200,
            "message": "Operation performed successfully"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DistrictGetView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        district=District.objects.all()
        serializer=DistrictSerializer(district,many=True)
        x={"success": "true",
        "status": 200,
        "message": "District Detail",
        "timestamp": time.time(),
        "district":serializer.data}
        return Response(x)

class ChildView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    # queryset = Child.objects.all()
    serializer_class = ChildSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            data = serializer.save()
            x = {"success": "true",
            "status": 200,
            "timestamp": time.time(),
            "message": "Operation performed successfully"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChildGetView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        child=Child.objects.all()
        serializer=ChildSerializer(child,many=True)
        x={"success": "true",
        "status": 200,
        "message": "Child Profile Detail",
        "timestamp": time.time(),
        "child_profile":serializer.data}
        return Response(x)

class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        x = {"success": "true",
            "status": 200,
            "message": "Operation performed successfully"}
        return Response(x,status=status.HTTP_200_OK)


class FileView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    # queryset = Child.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            data = serializer.save()
            x = {"success": "true",
            "status": 200,
            "timestamp": time.time(),
            "message": "Operation performed successfully"}
            return Response(x, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    