import json

from emailauth.models import auth
from emailauth.serializers import authSerializer

class AuthService : 
    def getAuth(userEmailAddr) :
        try : 
            serializer = authSerializer(auth.objects.filter(eamilAddress = userEmailAddr, verified = False), many=True)
            print(serializer.data)
            return serializer.data
        except :
            return RuntimeError

    def getLatestAuth() :
        try :
            latestData = auth.objects.latest('lastModifiedAt')
            return latestData.authCode
        except :
            return RuntimeError

    
    def addAuth(targetEmailAddr, randNum) :
        try :        
            print("add auth")
            newRow = auth(
                eamilAddress = targetEmailAddr,
                authCode = randNum
            )
            print(newRow)
            newRow.save()
            serializer = authSerializer(newRow)
            return serializer.data
        except :
            return RuntimeError