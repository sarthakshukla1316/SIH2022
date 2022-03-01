from django.db import models
from kex.brand.models import Brand
from kex.equipment_type.models import EquipmentType
from kex.users.models import User
from django.urls import reverse


def upload_location(instance, filename):
    return "/".join(["EquipmentImages", str(instance.title), filename])


condition_choice = (
    ("New", "New"),
    ("Used", "Used"),
)


class Equipment(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Brand, on_delete=models.CASCADE)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    equipment_location = models.CharField(max_length=200)
    description = models.TextField()
    daily_rental = models.IntegerField(default=0)
    hourly_rental = models.IntegerField(default=0)
    image_1 = models.ImageField(blank=True, upload_to=upload_location, null=True)
    image_2 = models.ImageField(blank=True, upload_to=upload_location, null=True)
    image_3 = models.ImageField(blank=True, upload_to=upload_location, null=True)
    image_4 = models.ImageField(blank=True, upload_to=upload_location, null=True)
    image_5 = models.ImageField(blank=True, upload_to=upload_location, null=True)
    available_start_time = models.DateField()
    available_end_time = models.DateField()
    model = models.CharField(max_length=200, blank=True)
    manufacturing_year = models.IntegerField(default=0)
    condition = models.CharField(
        max_length=200, choices=condition_choice, default="New"
    )
    Horsepower = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    show_phone_number = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("equipment:detail", kwargs={"id": self.id})
