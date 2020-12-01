from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *
from user.models import *
from django.db.models import Count

class HeadListView(View):
    def get(self, request):
        passengers = Passenger.objects.all()
        context = {
        'passengers' : passengers,
        }
        return render(request, 'head/headList.html', context)
  
    def post(self, request):
        if request.method == 'POST':
            #PASSENGER UPDATE
            if 'passengerUpdate' in request.POST:
                print('update profile button clicked')
                PassengerUsername = request.POST.get("passenger-username")
                PassengerFirstName = request.POST.get("passenger-firstName")
                PassengerMiddleName = request.POST.get("passenger-middleName")
                PassengerLastName = request.POST.get("passenger-lastName")
                PassengerEmailAddress = request.POST.get("passenger-emailAddress")
                PassengerPassword = request.POST.get("passenger-password")
                PassengerDepartment = request.POST.get("passenger-department")
                PassengerContactNumber = request.POST.get("passenger-contactNumber")
                PassengerGender = request.POST.get("passenger-gender")
                
                UpdatePassenger = Passenger.objects.filter(username = PassengerUsername).update(firstName = PassengerFirstName, middleName = PassengerMiddleName, lastName = PassengerLastName, emailAddress = PassengerEmailAddress, password = PassengerPassword, department = PassengerDepartment, contactNumber = PassengerContactNumber, gender = PassengerGender)
                
                print(UpdatePassenger)
                print('Passenger Updated')
            
            #PASSENGER DELETE
            elif 'passengerDelete' in request.POST:
                print('delete button clicked')
                getPassengerUsername = request.POST.get("deletePassenger-username")
                DeletePassenger = Passenger.objects.filter(username = getPassengerUsername).delete()
                print('recorded deleted')  
                
            #PASSENGER CASH IN
            elif 'passengerCashIn' in request.POST:
                getPassengerUsername = request.POST.get("cashInPassenger-username") 
                CashInUpdate = request.POST.get("cashIn-amount")
                AvailableBalance = request.POST.get("available-balance")
               
                if (AvailableBalance == 0) : 
                    AvailableBalanceUpdate = (int(AvailableBalance)-int(CashInUpdate))
                else :
                    AvailableBalanceUpdate = (int(AvailableBalance)+int(CashInUpdate))
                
                UpdatePassengerCashIn = Passenger.objects.filter(username = getPassengerUsername).update(availableBalance = AvailableBalanceUpdate, currentCashIn = CashInUpdate)
                print(UpdatePassengerCashIn)
                
        return redirect('head:headList_view')       

class HeadSummaryView(View):
    def get(self, request):
        return render(request, 'head/headSummary.html')
  
    def post(self, request):
        return render(request, 'head/headSummary.html')

class HeadDashboardWeekly(View):
    def get(self, request):
        allBuses = Bus.objects.count()
        allPassengers = Passenger.objects.count()
        context = {
            'allBuses' : allBuses, 
            'allPassengers' : allPassengers
        }
        return render(request, 'head/headDashboardWeekly.html', context)
  
    def post(self, request):
        return render(request, 'head/headDashboardWeekly.html')

class HeadDashboardMonthly(View):
    def get(self, request):
        allBuses = Bus.objects.count()
        allPassengers = Passenger.objects.count()
        context = {
            'allBuses' : allBuses,
            'allPassengers' : allPassengers
        }
        return render(request, 'head/headDashboardMonthly.html', context)
  
    def post(self, request):
        return render(request, 'head/headDashboardMonthly.html')

class HeadBusTransactionView(View):
    def get(self, request):
        qs_bus = Bus.objects.all()
        drivers = Driver.objects.all()
        context = {
            'buses' : qs_bus,
            'drivers' : drivers
        }
        return render(request, 'head/headBusTransaction.html', context)
  
    def post(self, request):
        if request.method == 'POST':
            #BUS UPDATE
            if 'busUpdate' in request.POST:
                bid = request.POST.get("bus-id")
                busBName = request.POST.get("bus-busName")
                busPNumber = request.POST.get("bus-plateNumber")
                busDes = request.POST.get("bus-destination")
                busSeats = request.POST.get("bus-totalSeats")
                busBsFare = request.POST.get("bus-busFare")
                busDTime = request.POST.get("bus-departureTime")
                UpdateBus = Bus.objects.filter(id=bid).update(busName = busBName, plateNumber = busPNumber, 
                            destination = busDes,totalSeats = busSeats, busFare = busBsFare, departureTime = busDTime)
                
            #BUS DELETE     
            elif 'busDelete' in request.POST:	          
                print('delete button clicked')
                bid = request.POST.get("deleteBus-id")
                deleteBus = Bus.objects.filter(id = bid).delete()
                print('recorded deleted') 
                
            #DRIVER UPDATE        
            elif 'driverUpdate' in request.POST:
                print('update profile button clicked')
                Driverid = request.POST.get("driver-id")
                DriverProfilePicture = request.POST.get("driver-profilePicture")
                DriverFirstName = request.POST.get("driver-firstName")
                DriverMiddleName = request.POST.get("driver-middleName")
                DriverLastName = request.POST.get("driver-lastName")
                DriverEmailAddress = request.POST.get("driver-emailAddress")
                DriverContactNumber = request.POST.get("driver-contactNumber")
                DriverGender = request.POST.get("driver-gender")
                    
                UpdateDriver = Driver.objects.filter(id = Driverid).update(firstName = DriverFirstName, middleName = DriverMiddleName, lastName = DriverLastName, emailAddress = DriverEmailAddress, contactNumber = DriverContactNumber, gender = DriverGender)
                    
                print(UpdateDriver)
                print('Driver Updated')  
                
            #DRIVER DELETE     
            elif 'driverDelete' in request.POST:	          
                print('delete button clicked')
                Driverid = request.POST.get("deleteDriver-id")
                DeleteDriver = Driver.objects.filter(id = Driverid).delete()
                print('recorded deleted') 

        return redirect('head:headBusTransaction_view')
       
class HeadRegisterBus(View):
    def get(self, request):
        return render(request, 'head/headRegisterBus.html')

    def post(self, request):

        form = BusForm(request.POST)

        if form.is_valid():

            busBName = request.POST.get("busName")
            busPNumber = request.POST.get("plateNumber")
            busDes = request.POST.get("destination")
            busSeats = request.POST.get("totalSeats")
            busBsFare = request.POST.get("busFare")
            busDTime = request.POST.get("departureTime")
            img = request.FILES.get('img')
            form = Bus(busName = busBName, plateNumber = busPNumber, destination = busDes,
                        totalSeats = busSeats, busFare = busBsFare, departureTime = busDTime, img = img)
            form.save()

            return redirect('head:headBusTransaction_view')

        else:
            print(form.errors)
            return HttpResponse('not valid')
class HeadRegisterDriver(View):
    def get(self, request):
        return render(request, 'head/headRegisterDriver.html')
  
    def post(self, request):
        form = RegisterDriverForm(request.POST, request.FILES)
    
        if form.is_valid():
            DriverProfilePicture = request.FILES.get('profilePicture')
            DriverFirstName = request.POST.get("firstName")
            DriverMiddleName = request.POST.get("middleName")
            DriverLastName = request.POST.get("lastName")
            DriverEmailAddress = request.POST.get("emailAddress")
            DriverContactNumber = request.POST.get("contactNumber")
            DriverGender = request.POST.get("gender")
    

            form = Driver(profilePicture = DriverProfilePicture, firstName = DriverFirstName, middleName = DriverMiddleName, lastName = DriverLastName, emailAddress = DriverEmailAddress, contactNumber = DriverContactNumber, gender = DriverGender)
            form.save()
        
            return redirect('head:headBusTransaction_view')   
        else:
            print(form.errors)
            return HttpResponse('not valid')
