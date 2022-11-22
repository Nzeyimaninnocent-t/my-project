from django.db import models

# Create your models here.
class businessdetail(models.Model):
    businessname = models.CharField(max_length=255)
    legalform = models.CharField(max_length=255)
    fiveyearobjective = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
class resources(models.Model):
    resource = models.CharField(max_length=255)
    proposedresource = models.CharField(max_length=255)
    purchaseditem = models.CharField(max_length=255)


class personnel(models.Model):
    keyperson = models.CharField(max_length=255)
    keypersonrole = models.CharField(max_length=255)
    keypersonresponsibilities = models.CharField(max_length=255) 

class market(models.Model):
    productserviceoffer = models.CharField(max_length=255)
    targetcustomers = models.CharField(max_length=255)
    geographicmarket = models.CharField(max_length=255)
    competitiveadvantage = models.CharField(max_length=255)


class competitor(models.Model):
    competitor = models.CharField(max_length=255)
    competitorweakness = models.CharField(max_length=255)
    competitiveadvantages = models.CharField(max_length=255)

class opportunity(models.Model):
    opportunity = models.CharField(max_length=255)           

class strategy(models.Model):
    strategicstep = models.CharField(max_length=255)
    methodofselling = models.CharField(max_length=255)
    advertising = models.CharField(max_length=255)

class finance(models.Model):
    currencysymbol = models.CharField(max_length=255)
    planstartyear = models.IntegerField()
    salesunitfreqperday = models.IntegerField()
    salesunitprice = models.IntegerField()
    salesperday= models.DecimalField(max_digits=10, decimal_places=2)
    salesyearone= models.DecimalField(max_digits=10, decimal_places=2)
    salesgrowthpercent = models.DecimalField(max_digits=10, decimal_places=2)
    cosofsales = models.DecimalField(max_digits=10, decimal_places=2)
    bankexpensesyearone = models.DecimalField(max_digits=10, decimal_places=2)
    depreciationexpensesyearone = models.DecimalField(max_digits=10, decimal_places=2)
    employeeexpensesyearone = models.DecimalField(max_digits=10, decimal_places=2)
    insuranceexpensesyearone = models.DecimalField(max_digits=10, decimal_places=2)
    marketingexpensesyearone = models.DecimalField(max_digits=10, decimal_places=2)
    officeexpensesyearone = models.DecimalField(max_digits=10, decimal_places=2)
    otherexpensesyearone = models.DecimalField(max_digits=10, decimal_places=2)
    premisesexpensesyearone = models.DecimalField(max_digits=10, decimal_places=2)
    professionaexpensesyearone = models.DecimalField(max_digits=10, decimal_places=2)
    shippingexpensesyearone = models.DecimalField(max_digits=10, decimal_places=2)
    travelexpensesyearone = models.DecimalField(max_digits=10, decimal_places=2)
    utilityexpensesyearone = models.DecimalField(max_digits=10, decimal_places=2)
    expensesyearone = models.DecimalField(max_digits=10, decimal_places=2)
    expensesgrowthpercent = models.DecimalField(max_digits=10, decimal_places=2)
    customerdayscredit = models.DecimalField(max_digits=10, decimal_places=2)
    supplierdayscredit = models.DecimalField(max_digits=10, decimal_places=2)
    equitycashinjection = models.DecimalField(max_digits=10, decimal_places=2)
    


        
