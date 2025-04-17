from django.db import models
from django.utils import timezone

# Create your models here.
class home(models.Model) :
    imgSrc = models.TextField()
    lastModifiedAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(default=timezone.now)

class about(models.Model) :
    section = models.TextField(null=True, blank=True)
    imgSrc = models.TextField(null=True, blank=True)
    title = models.TextField(default='')
    address = models.TextField(default='')
    content = models.TextField()
    InstagramId = models.TextField(null=True, blank=True)
    InstagramLink = models.TextField(null=True, blank=True)
    lastModifiedAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(default=timezone.now)

class cafe(models.Model) :
    section = models.TextField()
    img = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    lastModifiedAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(default=timezone.now)

class program(models.Model) :
    name = models.TextField()
    subName = models.TextField()
    img = models.TextField()
    content = models.TextField()
    introduction = models.TextField()
    lastModifiedAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(default=timezone.now)

class qna(models.Model) :
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    sortOrder = models.IntegerField()
    lastModifiedAt = models.DateTimeField(default=timezone.now)


# class soksoDetail(models.Model) :
#     topImages = models.TextField() 
#     contentImages = models.TextField()
#     content = models.TextField()
#     lastModifiedAt = models.DateTimeField(default=timezone.now)
#     createdAt = models.DateTimeField(default=timezone.now)


# class sokso(models.Model) :
#     level = models.IntegerField(default=1)
#     group = models.IntegerField(null=True, blank=True)
#     name = models.CharField(max_length=50)
#     introduction = models.TextField(null=True, blank=True)
#     mainImg = models.TextField()
#     soksoDetail_Id = models.ForeignKey(
#         soksoDetail,  on_delete=models.CASCADE, 
#         db_column="soksoDetail_Id", null=True, default=None
#     )
#     reserveLink = models.TextField(null=True, blank=True)
#     lastModifiedAt = models.DateTimeField(default=timezone.now)
#     createdAt = models.DateTimeField(default=timezone.now)

class stay(models.Model) :
    name = models.CharField(max_length=50)
    address = models.TextField()
    introduction1 = models.TextField(null=True, blank=True)
    introduction2 = models.TextField(null=True, blank=True)
    mainImgs = models.TextField() 
    optionAvailable = models.BooleanField() 
    lastModifiedAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(default=timezone.now)

class option(models.Model) :
    name = models.TextField(max_length=20)
    introduction = models.TextField(max_length=50)
    mainImgs = models.TextField() 
    content = models.TextField() 
    stay_id = models.ForeignKey(
        stay,  
        on_delete=models.CASCADE, 
        db_column="stay_id"
    )
    lastModifiedAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(default=timezone.now)

class room(models.Model) :
    name = models.CharField(max_length=50)
    structure = models.TextField()
    introduction1 = models.TextField(null=True, blank=True)
    introduction2 = models.TextField(null=True, blank=True)
    mainImgs = models.TextField() 
    content = models.TextField()
    stay_id = models.ForeignKey(
        stay,  
        on_delete=models.CASCADE, 
        db_column="stay_id"
    )
    layout = models.IntegerField(default=0)
    reserveLink = models.TextField(null=True, blank=True)
    reserveNumber = models.TextField(null=True, blank=True)
    lastModifiedAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(default=timezone.now)

# busniess
class busniess(models.Model) :
    id = models.IntegerField(primary_key=True)
    longtitude = models.TextField()
    latitude = models.TextField()
    addressText = models.TextField()
    runingHours = models.TextField()
    busniessNumber = models.TextField()
    instagramUrl = models.TextField()
    youtubeUrl = models.TextField()
    adminName = models.TextField()
    adminEmail = models.TextField()
    homeMiddleTitle = models.TextField(default='문화예술영성 공간')
    lastModifiedAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(default=timezone.now)

# class biz(models.Model) :
#     section = models.TextField()
#     name = models.TextField()
#     value = models.TextField()
#     note = models.TextField(null=True, blank=True)
#     lastModifiedAt = models.DateTimeField(default=timezone.now)
#     createdAt = models.DateTimeField(default=timezone.now)

class imageArchive(models.Model) :
    id = models.AutoField(primary_key=True)
    imgSrc = models.TextField()
    lastModifiedAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(default=timezone.now)

# class link(models.Model) :
#     name = models.TextField()
#     url = models.TextField()
#     lastModifiedAt = models.DateTimeField(default=timezone.now)
#     createdAt = models.DateTimeField(default=timezone.now)

class headerInfo(models.Model) :
    name = models.TextField()
    introduction1 = models.TextField(null=True, blank=True)
    introduction2 = models.TextField(null=True, blank=True)
    imgSrc = models.TextField()
    lastModifiedAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(default=timezone.now)