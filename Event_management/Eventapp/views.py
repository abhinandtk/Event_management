from django.shortcuts import render
from .models import UserRegister,UserLogin
from .serializers import RegisteruserSerializer,LoginuserSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate  # Import Django's authentication


# Create your views here.
class UserRegisterapi(GenericAPIView):
    serializer_class=LoginuserSerializer
    Register_serializer_class=RegisteruserSerializer
    def post(self,request):
     Log_id=''
     Name=request.data.get('Name')
     Contact=request.data.get('Contact')
     Email=request.data.get('Email')
     Username=request.data.get('Username')
     Password=request.data.get('Password')
     Email=request.data.get('Email')
     role='User'
     if(UserLogin.objects.filter(Username=Username)):
        return Response({'message':'Duplicate username found'},status.HTTP_400_BAD_REQUEST)
     else:
        serializer_login=self.serializer_class(data={'Username':Username,'Password':Password,'role':role})
        print(serializer_login)
        if(serializer_login.is_valid()):
           log=serializer_login.save()
           Log_id=log.id
        serializer=self.Register_serializer_class(data={'Name':Name,'Contact':Contact,'Email':Email,'Log_id':Log_id,})
        print(serializer)
        if(serializer.is_valid()):
           serializer.save()
           return Response({'data':serializer.data,'message':'User registered successfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'User registered failed','success':False},status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginpage(GenericAPIView):
   serializer_class=LoginuserSerializer
   def post(self,request):
      Username=request.data.get('Username')
      Password=request.data.get('Password')
      logreg=UserLogin.objects.filter(Username=Username,Password=Password)
      if(logreg.count()>0):
         read_serializer=LoginuserSerializer(logreg,many=True)
         for i in read_serializer.data:
            id=i['id']
            role=i['role']
         regdata=UserRegister.objects.all().filter(Log_id=id).values()
         print(regdata)
         for i in regdata:
            User_id=i['id']
            Name=i['Name']
            Contact=i['Contact']
            Email=i['Email']
         return Response({'data':{'Log_id':id,'role':role,'User_id':User_id,'Name':Name,'Contact':Contact,'Email':Email}})
      else:
         return Response({'data':'No data available','success':False},status=status.HTTP_400_BAD_REQUEST)






