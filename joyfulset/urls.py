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

from joyfulset.views import Home, Biz, Cafe, About, ImageArchive, Program, Qna, Sokso

urlpatterns = [
    path('edit-main-img/', About.editMainImg , name='edit-main-img'),
    
    path('home/get/', Home.get , name='home/get'),
    path('home/add/', Home.add , name='home/add'),
    path('home/delete/', Home.delete , name='home/delete'),

    path('about/get/', About.get , name='about/get'),
    path('about/get-by-section/', About.getBySection , name='about/get-by-section'),
    path('about/get-main-img/', About.getMainImg , name='about/get-main-img'),
    path('about/update/contents/', About.updateContents , name='about/update/contents'),

    path('cafe/getAll/', Cafe.getAll , name='cafe/getAll'),
    path('cafe/getBySection/', Cafe.getBySection , name='cafe/getBySection'),
    path('cafe/create/', Cafe.createCafe , name='cafe/create'),
    path('cafe/updateCafe/', Cafe.updateCafe , name='cafe/updateCafe'),
    path('cafe/deleteById/', Cafe.deleteById , name='cafe/deleteById'),

    path('program/getAll/', Program.getAll , name='program/getAll'),
    path('program/create/', Program.createProgram , name='program/create'),
    path('program/update/', Program.updateProgram , name='program/update'),
    path('program/deleteById/', Program.deleteById , name='program/deleteById/'),

    path('qna/get/', Qna.getQna , name='qna/get/'),
    path('qna/add/', Qna.add , name='qna/get/'),
    path('qna/upseart/', Qna.upseart , name='qna/upseart/'),
    path('qna/delete/', Qna.deleteQna , name='qna/delete/'),
    path('qna/edit-sort-order/', Qna.editSortOrder , name='qna/edit-sort-order/'),

    path('biz/get/', Biz.get , name='home/get'),
    path('biz/getAll/', Biz.getAll , name='biz/getAll'),
    path('biz/getBySection/', Biz.getBySection , name='home/getBySection'),
    path('biz/get-kakao/', Biz.getKakao , name='home/get-kakao'),
    path('biz/update/', Biz.editBiz , name='home/update'),

    path('sokso/getById/', Sokso.getById , name='sokso/getById'), 
    path('sokso/getByLevel/', Sokso.getByLevel , name='sokso/getByLevel'), 
    path('sokso/getByLevelAndGroup/', Sokso.getByLevelAndGroup , name='sokso/getByLevelAndGroup'), 
    path('sokso/upseart/', Sokso.upsertSokso , name='sokso/upseart/'),
    path('sokso/deleteById/', Sokso.deleteById , name='sokso/deleteById/'),
    
    path('imageArchive/getAll/', ImageArchive.getAll , name='imageArchive/getAll/'),
    path('imageArchive/upload/', ImageArchive.upload , name='imageArchive/upload/'),
    path('imageArchive/replace/', ImageArchive.replace , name='imageArchive/replace/'),
    path('imageArchive/deleteByImageName/', ImageArchive.deleteByImageName , name='imageArchive/deleteByImageName/'),

    path('upload-img-with-deletion/', About.uploadImageWithDeletion , name='upload-img-with-deletion'),
]


