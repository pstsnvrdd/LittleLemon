from django.db import models

#Booking model
class Booking(models.Model):
    name = models.CharField(max_length=200)
    booking_date = models.DateField()
    no_of_guests = models.SmallIntegerField(default=1)

    def __str__(self): 
        return self.name


#Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.DecimalField(max_digits=5, decimal_places=2) 
   inventory = models.IntegerField() 

   def __str__(self):
      return f'{self.name} : {str(self.price)}'
