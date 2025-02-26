import random
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from emailauth.service.AuthService import AuthService
from emailauth.service.CustomEmailService import CustomEmailService

# Create your views here.
class Auth : 
    @api_view(['GET'])
    def checkAuth(request) :
        try :
            inputAuthCode = request.GET.get("inputAuthCode")
            verified = False
            return_data = AuthService.getLatestAuth()
            print("getLatestAuth" , return_data)
            if return_data == inputAuthCode :
                verified = True
            
            return Response(verified, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['GET'])
    def sendAuth(request) :
        try :
            userEmailAddr = request.GET.get("userEmailAddr")
            print(userEmailAddr)
            # step1 generate random number 
            randNum = random.randint(100000,999999)
            print(randNum)
            # step 2 send to database
            AuthService.addAuth(userEmailAddr, randNum)
            # step 3 send email
            result = CustomEmailService.sendAuth(userEmailAddr, randNum)
            print("result : ",result)
            return Response(result, status = status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['GET'])
    def sendRecoverRequest(request) :
        try :
            content = request.GET.get("content")
            ipAddress = request.GET.get("ipAddress")
            requestingPerson = request.GET.get("requestingPerson")

            print(content)
            print(ipAddress)
            print(requestingPerson)
            
            result = CustomEmailService.sendRecoverRequest(content, ipAddress, requestingPerson)
            return Response(result, status = status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)