from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    credits = models.IntegerField(default=50)

    def __str__(self):
        return self.email


class Course(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_public = models.BooleanField(default=False)
    # Add other fields as per your requirements

    def __str__(self):
        return self.title


class Topic(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add other fields as per your requirements

    def __str__(self):
        return self.title


class Block(BaseModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    code = models.TextField()
    tips = models.TextField()
    # Add other fields as per your requirements

    def __str__(self):
        return self.title