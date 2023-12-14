from django.db import models

job_nature = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance, filename):
    extension = filename.split(".")
    return f"jobs/{instance.id}.{extension}"

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15,
                                choices=job_nature)
    description = models.TextField(max_length=1500)
    published_at = models.DateField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.title
    

