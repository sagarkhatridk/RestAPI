from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class ToDo(BaseModel):
    objects = None
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    Todo_Title = models.CharField(max_length=100)
    Todo_Description = models.TextField()
    is_Done = models.BooleanField(default=False)


class TimingTodo(BaseModel):
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE)
    timing = models.DateField()
