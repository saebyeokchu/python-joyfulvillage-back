"""
URL configuration for deformback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from joyfulset.views import Busniess, HeaderInfo, Home, Cafe, About, ImageArchive, Option, Program, Qna, Room,Stay

urlpatterns = [
    # path('edit-main-img/', Home.editMainImg , name='edit-main-img'),
    
    path('home/get/', Home.get , name='home/get'),
    path('home/getMiddleTitle/', Home.getMiddleTitle , name='home/getMiddleTitle'),
    path('home/updateMiddleTitle/', Home.updateMiddleTitle , name='home/updateMiddleTitle'),
    path('home/add/', Home.add , name='home/add'),
    path('home/deleteById/', Home.deleteById , name='home/deleteById'),

    path('about/get_by_id/', About.get_by_id , name='about/get_by_id'),
    path('about/getAll/', About.getAll , name='about/getAll'),
    path('about/getBySection/', About.getBySection , name='about/getBySection'),
    path('about/upsert/', About.upsert , name='about/upsert'),
    path('about/deleteById/', About.deleteById , name='about/deleteById'),

    path('cafe/getAll/', Cafe.getAll , name='cafe/getAll'),
    path('cafe/getBySection/', Cafe.getBySection , name='cafe/getBySection'),
    path('cafe/create/', Cafe.createCafe , name='cafe/create'),
    path('cafe/updateCafe/', Cafe.updateCafe , name='cafe/updateCafe'),
    path('cafe/deleteById/', Cafe.deleteById , name='cafe/deleteById'),

    path('program/get_by_id/', Program.get_by_id , name='program/get_by_id'),
    path('program/getAll/', Program.getAll , name='program/getAll'),
    path('program/create/', Program.createProgram , name='program/create'),
    path('program/update/', Program.updateProgram , name='program/update'),
    path('program/deleteById/', Program.deleteById , name='program/deleteById/'),

    path('qna/get/', Qna.getQna , name='qna/get/'),
    path('qna/add/', Qna.add , name='qna/get/'),
    path('qna/upseart/', Qna.upseart , name='qna/upseart/'),
    path('qna/delete/', Qna.deleteQna , name='qna/delete/'),
    path('qna/edit-sort-order/', Qna.editSortOrder , name='qna/edit-sort-order/'),

    path('biz/get/', Busniess.get , name='home/get'),
    # path('biz/getAll/', Biz.getAll , name='biz/getAll'),
    # path('biz/getBySection/', Biz.getBySection , name='home/getBySection'),
    path('biz/get-kakao/', Busniess.getKakao , name='home/get-kakao'),
    path('biz/update/', Busniess.editBiz , name='home/update'),

    
    path('imageArchive/getAll/', ImageArchive.getAll , name='imageArchive/getAll/'),
    path('imageArchive/uploadImage/', ImageArchive.uploadImage , name='imageArchive/uploadImage/'),
    path('imageArchive/replace/', ImageArchive.replace , name='imageArchive/replace/'),
    path('imageArchive/deleteByImageName/', ImageArchive.deleteByImageName , name='imageArchive/deleteByImageName/'),

    # path('upload-img-with-deletion/', Home.uploadImageWithDeletion , name='upload-img-with-deletion'),
    path('stay/getById/', Stay.getById , name='stay/getById'), 
    path('stay/getAll/', Stay.getAll , name='stay/getAll'), 
    path('stay/upsert/', Stay.upsertStay , name='stay/upsert/'),
    path('stay/deleteById/', Stay.deleteById , name='stay/deleteById/'),
    
    path('option/getById/', Option.getById , name='option/getById'), 
    path('option/getAll/', Option.getAll , name='option/getAll'), 
    path('option/getByStayId/', Option.getByStayId , name='option/getByStayId'), 
    path('option/upsert/', Option.upsertOption , name='option/upsert/'),
    path('option/deleteById/', Option.deleteById , name='option/deleteById/'),

    # path('link/getAll/', Link.getAll , name='link/getAll'), 
    # path('link/upseart/', Link.upsertLink , name='link/upseart/'),
    # path('link/deleteById/', Link.deleteById , name='link/deleteById/'),

    path('room/getById/', Room.getById , name='room/getById'), 
    path('room/getAll/', Room.getAll , name='room/getAll'), 
    path('room/getByStayId/', Room.getByStayId , name='room/getByStayId'), 
    path('room/upseart/', Room.upsertRoom , name='room/upseart/'),
    path('room/deleteById/', Room.deleteById , name='room/deleteById/'),

    path('header_info/get_info_by_id/', HeaderInfo.get_info_by_id , name='header_info/get_info_by_id'),
    path('header_info/getAll/', HeaderInfo.getAll , name='header_info/getAll'),
    path('header_info/upsert/', HeaderInfo.upsert , name='header_info/upsert'),


]


