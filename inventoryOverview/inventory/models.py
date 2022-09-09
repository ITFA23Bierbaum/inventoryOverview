from django.db import models


# Create your models here.
class Shelf(models.Model):
    id = models.IntegerField(primary_key=True)
    row = models.IntegerField()
    section = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return f"Reihe:{self.row}, Abschnitt:{self.section}, Etage:{self.height}"


class InventoryItem(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    stock = models.IntegerField()
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number}, {self.name}, {self.stock}, {self.shelf}"


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number}, {self.customer}"


class OrderItem(models.Model):
    inventoryItem = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    amount = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
