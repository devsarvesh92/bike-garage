from django.db import models
import uuid


# Create your models here.
class ModelBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Brand(ModelBase):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True, blank=False, db_index=True)

    class Meta:
        ordering = ["name"]


class Model(ModelBase):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4(), unique=True)
    name = models.CharField(max_length=200, unique=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class ModelInfo(Model):
    cc = models.IntegerField()
    price = models.DecimalField(unique=False, max_digits=5, decimal_places=2)


class City(ModelBase):
    name = models.CharField(max_length=200, unique=True)

