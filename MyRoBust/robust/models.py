from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .models import *

# class User(models.Model):
#         name = models.CharField(max_length = 100,null = True)
#         email = models.CharField(max_length = 100,null = True)
#         phone = models.CharField(max_length = 100,null = True)
#         date_created = models.DateTimeField(auto_now_add = True,null = True)
#         profile_pic = models.ImageField(upload_to = 'media/')
        
#         def __str__(self):
#             return self.name
        
#class Passenger(models.Model):
#        username = models.CharField(max_length = 100, primary_key = True, null=False)
#        firstName = models.CharField(max_length = 100)
#        middleName = models.CharField(max_length = 100)
#        lastName = models.CharField(max_length = 100)
#        emailAddress = models.EmailField()
#        contactNumber = models.CharField(max_length = 100)
#        department = models.CharField(max_length = 100)
#        gender = models.CharField(max_length = 100)
#        password = models.CharField(max_length = 15)
#        availableBalance = models.IntegerField()
#        currentCashIn = models.IntegerField()
#
#        class Meta:
#            db_table = "Passenger"

#class Admin(models.Model):
#        username = models.CharField(max_length = 50, primary_key = True)
#        password = models.CharField(max_length = 50)
#        firstName = models.CharField(max_length = 50)
#        middleName = models.CharField(max_length = 50)
#        lastName = models.CharField(max_length = 50)
#        emailAddress = models.CharField(max_length = 50)
#        contactNumber = models.IntegerField()
#        username = models.CharField(max_length = 50, primary_key = True)
#        password = models.CharField(max_length = 50)
#
#        class Meta:
#            db_table = "Admin"

class EWallet(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
        availableBalance = models.IntegerField(default = 0)
        currentCashIn = models.IntegerField(default = 0)

        class Meta:
            db_table = "EWallet"

class Driver(models.Model):
#        driverID = models.AutoField(primary_key=True)
        userLogIn = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
        profilePicture = models.ImageField(upload_to='imagesDriver/', null=True, blank=True)
        firstName = models.CharField(max_length = 50)
        middleName = models.CharField(max_length = 50)
        lastName = models.CharField(max_length = 50)
        emailAddress = models.CharField(max_length = 50)
        contactNumber = models.CharField(max_length = 50)
        gender = models.CharField(max_length = 20)

        class Meta:
            db_table = "Driver"
                   
class Bus(models.Model):
        busID=models.AutoField(primary_key=True)
        busName = models.CharField(max_length = 50)
        plateNumber = models.CharField(max_length = 50)
        destination = models.CharField(max_length = 50)
        totalSeats = models.PositiveSmallIntegerField(default=51)
        busFare = models.PositiveSmallIntegerField(default=0)
        departureTime = models.TimeField(default = timezone.now)
        img = models.ImageField(upload_to='imagesBus/', null=True, blank=True)
#        driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    
        class Meta:
            db_table = "Bus"

class Booking(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
        date_booked = models.DateField(auto_now_add = True)
        booking=models.AutoField(primary_key=True, null=False)
        bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
        seatNumber = models.CharField(max_length = 15)
        dateReservation = models.DateField(default = None)
    
        class Meta:
            db_table = "Booking"

        # def __str__(self):
        #     return self.user.username +" | "+ self.booking.bus.busName +" | "+ self.seatNumber
            
class DashboardBus(models.Model):
#       user_ID = models.ForeignKey(Bus, on_delete=models.CASCADE)
        totalBuses = models.IntegerField()
        userLogIn = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
        is_deleted = models.BooleanField(default=False)
        
        class Meta:
            db_table = "DashboardBus"   
            
class DashboardUser(models.Model):
#        bus_ID = models.ForeignKey(Bus, on_delete=models.CASCADE)
        totalUsers = models.IntegerField()
        userLogIn = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
        is_deleted = models.BooleanField(default=False)
        
        class Meta:
            db_table = "DashboardUser" 
        