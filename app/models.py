from django.db import models

class bank(models.Model):
    ifsc=models.CharField(max_length=255)

    def __str__(self):
        return self.ifsc

class b_city(models.Model):
    city=models.CharField(max_length=255)
    b_name=models.CharField(max_length=255)

    def __str__(self):
        return self.b_name