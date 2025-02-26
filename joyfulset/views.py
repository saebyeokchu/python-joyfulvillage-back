import os
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from api import ImageApi
from joyfulset.service.ProgramService import ProgramService
from joyfulset.service.CafeService import CafeService
from joyfulset.service.ImageArchiveService import ImageArchiveService
from joyfulset.service.HomeService import HomeService
from joyfulset.service.QnaService import QnaService
from joyfulset.service.BizService import BizService
from joyfulset.service.SoksoService import SoksoService


# Create your views here.
class Home : 
    @api_view(['get'])
    def get(request) :
        try :
            return_data = HomeService.get()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['get'])
    def add(request) :
        try :
            src = request.GET.get("src")
            if src :
                return_data = HomeService.add(src)
                return Response({"success": True, "data": return_data}, status=status.HTTP_200_OK)
        except :
            return Response({"success": False},status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    @api_view(['get'])
    def delete(request) :
        try :
            id = request.GET.get("id")
            if id :
                return_data = HomeService.delete(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class About : 
    @api_view(['post'])
    def uploadImageWithDeletion(request) :
        try :
            if request.method == "POST" and request.FILES.get("image"):
                image = request.FILES["image"]
                imageName = request.data.get("imageName") 
                folderName = request.data.get("folderName")

                external_folder_path = r"C:/Users/cuu02/OneDrive/바탕 화면/joyful/code/joyful/public/system/" + folderName

                # Ensure the directory exists
                os.makedirs(external_folder_path, exist_ok=True)

                # Define the full file path
                file_path = os.path.join(external_folder_path, imageName)

                # Save the file
                with open(file_path, 'wb') as f:
                    for chunk in image.chunks():
                        f.write(chunk)

                # file_path = default_storage.save(f"uploads/{image.name}", ContentFile(image.read()))

                # {"message": "Image uploaded successfully!", "file_path": file_path}
                return Response(file_path, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['post'])
    def editMainImg(request) :
        try :
            return Response(status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def get(request) :
        try :
            return_data = HomeService.get()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def getBySection(request) :
        try :
            if request.method == "GET" and request.data.get("section") :
                return_data = HomeService.getBySection(request.data.get("section") )
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def getMainImg(request) :
        try :
            return_data = HomeService.getMainImg()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['post'])
    def updateContents(request) :
        try :
            if request.method == "POST" and request.data.get("section") and request.data.get("contents"):
                section = request.data.get("section") 
                contents = request.data.get("contents")
                updateSuccess = HomeService.updateContents(section, contents)
                if updateSuccess :
                    return Response(status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class Cafe : 
    @api_view(['get'])
    def getAll(request) :
        try :
            return_data = CafeService.getAll()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def getBySection(request) :
        try :
            if request.method == "GET" and request.GET.get("section") :
                return_data = CafeService.getBySection(request.GET.get("section"))
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response({ "success" : False } ,status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['post'])
    def createCafe(request) :
        try :
            if request.method == "POST" and request.data.get("data") :
                data = request.data.get("data") 
                updateSuccess = CafeService.create(data)
                if updateSuccess :
                    return Response(True,status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['post'])
    def updateCafe(request) :
        try :
            if request.method == "POST" and request.data.get("data") :
                data = request.data.get("data") 
                updateSuccess = CafeService.updateCafe(data)
                if updateSuccess :
                    return Response({ "success" : True },status=status.HTTP_200_OK)
        except :
            return Response({ "success" : True },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['get'])
    def deleteById(request) :
        print("[deleteById]")
        try :
            id = request.GET.get("id")
            if id :
                return_data = CafeService.deleteById(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response({ "success" : False },status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class Program : 
    @api_view(['get'])
    def getAll(request) :
        try :
            return_data = ProgramService.getAll()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['post'])
    def createProgram(request) :
        try :
            if request.method == "POST" and request.data.get("data") :
                data = request.data.get("data") 
                result = ProgramService.create(data)
                if result :
                    return Response(True,status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['post'])
    def updateProgram(request) :
        try :
            if request.method == "POST" and request.data.get("data") :
                data = request.data.get("data") 
                updateSuccess = ProgramService.updateProgram(data)
                if updateSuccess :
                    return Response(True,status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    @api_view(['get'])
    def deleteById(request) :
        print("[deleteById]")
        try :
            id = request.GET.get("id")
            if id :
                return_data = ProgramService.deleteById(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class Qna :
    @api_view(['get'])
    def getQna(request) :
        try :
            return_data = QnaService.get()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['post'])
    def add(request) :
        try :
            answer = request.data.get("answer") 
            question = request.data.get("question")

            if answer and question :
                print(answer, question)
                return_data = QnaService.insertQna(answer,question)
                print(return_data)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['post'])
    def upseart(request) :
        try :
            qna = request.data.get("qna") 
            if qna :
                QnaService.upsertQna(qna)
                return_data = QnaService.get()
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
      
    @api_view(['post'])
    def deleteQna(request) :
        try :
            id = request.data.get("id") 

            if id :
                QnaService.delete_qna_entry(id)
                return_data = QnaService.get()
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['post'])
    def editSortOrder(request) :
        try :
            order = request.data.get("order") 
            
            QnaService.update_qna_sort_order(order)
            return_data = QnaService.get()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class Biz :
    @api_view(['get'])
    def get(request) :
        try :
            return_data = BizService.get()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['get'])
    def getAll(request) :
        try :
            return_data = BizService.getAll()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['get'])
    def getBySection(request) :
        try :
            section = request.data.get("section")
            if request.method == "GET" and section :
                return_data = BizService.getBySection(section)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def getKakao(request) :
        try :
            return_data = BizService.getKakao()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['post'])
    def editBiz(request) :
        try :
            long = request.data.get("long") 
            lan = request.data.get("lan") 
            addressText = request.data.get("addressText") 

            result = BizService.updateBiz(long, lan, addressText)
            if result : 
                return_data = BizService.get()
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class Sokso :
    @api_view(['get'])
    def getById(request) :
        print("[getById]")
        try :
            id = request.GET.get("id")
            if id :
                return_data = SoksoService.getById(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def getByLevel(request) :
        print("[getByLevel]")
        try :
            level = request.GET.get("level")
            if level :
                return_data = SoksoService.getByLevel(level)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def getByLevelAndGroup(request) :
        print("[getByLevelAndGroup]")
        try :
            level = request.GET.get("level")
            group = request.GET.get("group")
            if level and group :
                return_data = SoksoService.getByLevelAndGroup(level, group)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['post'])
    def upsertSokso(request) :
        print("[upsertSokso]")
        try :
            data = request.data.get("data") 
            if data :
                return_data = SoksoService.upsert(data)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def deleteById(request) :
        print("[deleteById]")
        try :
            id = request.GET.get("id")
            if id :
                return_data = SoksoService.deleteById(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class ImageArchive :
    @api_view(['get'])
    def getAll(request) :
        try :
            return_data = ImageArchiveService.getAll()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['post'])
    def upload(request) :
        try :
            if request.method == "POST" and request.FILES.get("image"):
                image = request.FILES["image"]
                imageName = request.data.get("imageName") 
                print(imageName)
                imageUploadResult = ImageApi.upload_image(image, imageName)

                if imageUploadResult :
                    newFileName = imageUploadResult["new_image_name"]
                    # add image to database
                    createResult = ImageArchiveService.create(newFileName)
                    return Response(createResult, status=status.HTTP_200_OK)
                return Response(newFileName, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['post'])
    def replace(request) :
        try :
            print("replace")
            print(request.FILES)
            if request.method == "POST" and request.FILES.get("image"):
                image = request.FILES["image"]
                previous_path = request.data.get("previousPath") 
                print(previous_path)
                imageUploadResult = ImageApi.replace_image(previous_path, image)

                if imageUploadResult :
                    return Response({ "success" : True }, status=status.HTTP_200_OK)
                return Response({ "success" : False }, status=status.HTTP_200_OK)
        except :
            return Response({ "success" : False }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['post'])
    def deleteByImageName(request) :
        try :
            name = request.data.get("name")
            id = request.data.get("id")
            print(name, id)
            if name and id:
                # remove image itself first
                imageDeletionResult = ImageApi.delete_image(name)

                if imageDeletionResult["result"] :
                    #remove image archive database after
                    dbResult = ImageArchiveService.deleteById(id)
                    if dbResult :
                        returnData = ImageArchiveService.getAll()
                        return Response(returnData, status=status.HTTP_200_OK)
        except :
            return Response({ "success" : False },status = status.HTTP_500_INTERNAL_SERVER_ERROR)