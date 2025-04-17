import os
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from api import ImageApi
from joyfulset.service.AboutService import AboutService
from joyfulset.service.OptionService import OptionService
from joyfulset.service.RoomService import RoomService
from joyfulset.service.StayService import StayService
from joyfulset.service.ProgramService import ProgramService
from joyfulset.service.CafeService import CafeService
from joyfulset.service.ImageArchiveService import ImageArchiveService
from joyfulset.service.HomeService import HomeService
from joyfulset.service.QnaService import QnaService
from joyfulset.service.BusniessService import BusniessService
from joyfulset.service.HeaderInfoService import HeaderInfoService


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
    def getMiddleTitle(request) :
        print("getMiddleTitle")
        try :
            return_data = HomeService.getMiddleTitle()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['post'])
    def updateMiddleTitle(request) :
        print("updateMiddleTitle")
        try :
            middle_text = request.data["middle_title"]
            if middle_text :
                return_data = HomeService.updateMiddleTitle(middle_text)
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
    def deleteById(request) :
        print("deleteById")
        try :
            id = request.GET.get("id")
            print("id : ",id)
            if id :
                return_data = HomeService.deleteById(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class About : 
    @api_view(['get'])
    def get_by_id(request) :
        print("[About : get_by_id]")
        try :
            id = request.GET.get("id")
            if id :
                return_data = AboutService.get_about_by_id(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def getAll(request) :
        try :
            return_data = AboutService.getAll()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def getBySection(request) :
        try :
            if request.method == "GET" and request.data.get("section") :
                return_data = AboutService.getBySection(request.data.get("section") )
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['post'])
    def upsert(request) : 
        try :
            print("upsetrt")
            data = request.data.get("data")

            if request.method == "POST" and data:
                updateSuccess = AboutService.upsert(data)
                if updateSuccess :
                    return Response({ "success" : True }, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    @api_view(['get'])
    def deleteById(request) :
        print("[deleteById]")
        try :
            id = request.GET.get("id")
            if id :
                return_data = AboutService.deleteById(id)
                return Response(return_data, status=status.HTTP_200_OK)
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
    def get_by_id(request) :
        print("[Program : get_by_id]")
        try :
            id = request.GET.get("id")
            if id :
                return_data = ProgramService.get_program_by_id(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
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
        
class Busniess :
    @api_view(['get'])
    def get(request) :
        try :
            return_data = BusniessService.get()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['get'])
    def getKakao(request) :
        try :
            return_data = BusniessService.getKakao()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['post'])
    def editBiz(request) :
        try :
            long = request.data.get("long") 
            lan = request.data.get("lan") 
            addressText = request.data.get("addressText") 

            result = BusniessService.updateBiz(long, lan, addressText)
            if result : 
                return_data = BusniessService.get()
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
    def uploadImage(request) :
        try :
            print("uploadImage")

            if request.method == "POST" and request.FILES["image"]:
                image = request.FILES["image"]
                imageName = request.data.get("imageName") 
                print(imageName)

                imageUploadResult = ImageApi.upload_image(image, imageName)

                if imageUploadResult :
                    new_image_name = imageUploadResult["new_image_name"]
                    image_url = imageUploadResult["image_url"]

                    # add image to database
                    create_result = ImageArchiveService.create(new_image_name)
                    return Response(
                        create_result,
                        status=status.HTTP_200_OK
                    )
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
    
class Stay :
    @api_view(['get'])
    def getById(request) :
        try :
            id = request.GET.get("id")
            if id :
                return_data = StayService.get_stay_by_id(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def getAll(request) :
        try :
            return_data = StayService.getAll()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['post'])
    def upsertStay(request) :
        print("[upsertStay]")
        try :
            data = request.data.get("data") 
            if data :
                return_data = StayService.upsert(data)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def deleteById(request) :
        print("[deleteById]")
        try :
            id = request.GET.get("id")
            if id :
                return_data = StayService.deleteById(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class Option :
    @api_view(['get'])
    def getById(request) :
        try :
            print("getById")
            id = request.GET.get("id")
            if id :
                return_data = OptionService.getById(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR) 
    

    @api_view(['get'])
    def getAll(request) :
        try :
            return_data = OptionService.getAll()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
    @api_view(['get'])
    def getByStayId(request) :
        try :
            stay_id = request.GET.get("id")
            if stay_id :
                return_data = OptionService.getByStayId(stay_id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['post'])
    def upsertOption(request) :
        print("[upsertOption]")
        try :
            data = request.data.get("data") 
            if data :
                return_data = OptionService.upsert(data)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def deleteById(request) :
        print("[deleteById]")
        try :
            id = request.GET.get("id")
            if id :
                return_data = OptionService.deleteById(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class Room :
    @api_view(['get'])
    def getById(request) :
        try :
            id = request.GET.get("id")
            print("[id]",id)
            if id :
                return_data = RoomService.get_room_by_id(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def getAll(request) :
        print("[getAll]")
        try :
            return_data = RoomService.getAll()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @api_view(['get'])
    def getByStayId(request) :
        try :
            stay_id = request.GET.get("id")
            if stay_id :
                return_data = RoomService.getByStayId(stay_id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
   
    @api_view(['post'])
    def upsertRoom(request) :
        print("[upsertRoom]")
        try :
            data = request.data.get("data") 
            print(data)
            if data :
                return_data = RoomService.upsert(data)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def deleteById(request) :
        print("[deleteById]")
        try :
            id = request.GET.get("id")
            if id :
                return_data = RoomService.deleteById(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class HeaderInfo : 
    @api_view(['get'])
    def get_info_by_id(request) :
        print("[AbHeaderInfoout : get_info_by_id]")
        try :
            id = request.GET.get("id")
            if id :
                return_data = HeaderInfoService.get_info_by_id(id)
                return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['get'])
    def getAll(request) :
        try :
            return_data = HeaderInfoService.getAll()
            return Response(return_data, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @api_view(['post'])
    def upsert(request) : 
        try :
            data = request.data.get("data")

            if request.method == "POST" and data:
                updateSuccess = HeaderInfoService.upsert(data)
                if updateSuccess :
                    return Response({ "success" : True }, status=status.HTTP_200_OK)
        except :
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)