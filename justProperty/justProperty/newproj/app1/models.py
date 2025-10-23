from django.db import models

# Create your models here.
class tblProperty(models.Model):
    PropertyID = models.AutoField(primary_key=True)
    PropertyHouseNumber = models.IntegerField()
    PropertyPostcode = models.CharField(max_length=6)
    #PropertyTypeID = models.ForeignKey(tblPropertyType, on_delete=models.CASCADE)
    Bedrooms = models.IntegerField()

    def __str__(self):
        return self.PropertyPostcode