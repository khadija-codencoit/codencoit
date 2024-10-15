from django.db import models



class Industry(models.Model):
    
    name = models.CharField(max_length=255)
    icon = models.FileField(upload_to="/industry_icon/")
    short_describtion = models.CharField(max_length=255)
    createf_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

 

class Projects(models.Model):
    title = models.CharField(max_length=255)
    short_describtion = models.CharField(max_length=255)
    long_describtion = models.CharField(max_length=255)
    clint_statement = models.CharField(max_length=255)
    clint_picture = models.FileField(upload_to= "/client_pic/")
 
   
class ProjectImage(models.Model):
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    image = models.FileField(upload_to="/project_pic/")  
    
    
class Services(models.Model):
    icon = models.FileField(upload_to="/service_icon")
    name = models.CharField(max_length=255)
    describtion = models.CharField(max_length=255)
    createf_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class ServiceProduct(models.Model):
    service_id = models.ForeignKey(Services,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)

   
class Technologies(models.Model):
    name = models.CharField(max_length=255)
    icon = models.FileField(upload_to="/tech_icon/")
    picture = models.FileField(upload_to="/tech_pic/")
    short_describtion = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class TechnologiesProduct(models.Model):
    tech_id = models.ForeignKey(Technologies,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    
    
class Fields(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class FieldsProduct(models.Model):
    field_id = models.ForeignKey(Fields,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    
    