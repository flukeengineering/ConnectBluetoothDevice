from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from connectdevice.models import ConnectDevice
from django.contrib.auth.models import User
from connectdevice.api.serializers import ConnectDeviceSerializer, UserCreateSerializer

class UserRegister(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class ConnectDeviceList(generics.ListCreateAPIView):
    queryset = ConnectDevice.objects.all()
    serializer_class = ConnectDeviceSerializer

class ConnectDeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConnectDevice.objects.all()
    serializer_class = ConnectDeviceSerializer

@api_view(["GET","POST"])
def connectdevice_list_create_api_view(request):
    if request.method == "GET":
        connect = ConnectDevice.objects.all()
        serializer = ConnectDeviceSerializer(connect, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ConnectDeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def connectdevice_list_update_api_view(request, pk):
    try:
        connect = ConnectDevice.objects.get(pk=pk)
    except ConnectDevice.DoesNotExist:
        return Response(
            {"error": {
                "code": 404,
                "message": "Device not found!"
            }}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        serializer = ConnectDeviceSerializer(connect)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ConnectDeviceSerializer(connect, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        connect.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET","POST"])
def user_list_create_api_view(request):
    if request.method == "GET":
        user = User.objects.all()
        serializer = UserCreateSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)