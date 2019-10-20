from django.db import models
from django.urls import reverse


class Product(models.Model):

    #  Fields
    Name = models.TextField(max_length=100)
    Description = models.TextField(max_length=300)
    Size = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    Price = models.FloatField()
    PublicProductId = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_Product_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_Product_update", args=(self.pk,))


class EmailTemplate(models.Model):

    #  Relationships
    M_T_M_Priviliges_Emails = models.ManyToManyField("undefined.PriviligeLevel")

    #  Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    Type = models.TextField(max_length=60)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_EmailTemplate_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_EmailTemplate_update", args=(self.pk,))


class PriviligeLevel(models.Model):

    #  Relationships
    M_T_M_Priviligies_Emails2 = models.ManyToManyField("undefined.EmailTemplate")

    #  Fields
    Name = models.TextField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    GrantsAccessTo = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_PriviligeLevel_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_PriviligeLevel_update", args=(self.pk,))


class Transaction(models.Model):

    #  Relationships
    O_T_O_Order_Transaction = models.OneToOneField("undefined.Order")

    #  Fields
    PaymentType = models.TextField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    WasPayback = models.BooleanField()
    PaymentOption = models.TextField(max_length=100)
    Amount = models.FloatField()
    Currency = models.TextField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_Transaction_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_Transaction_update", args=(self.pk,))


class OrderItem(models.Model):

    #  Relationships
    O_T_M_Order_OrderItems = models.ForeignKey("undefined.Order", on_delete=models.CASCADE)
    O_T_M_Product_OrderItems2 = models.ForeignKey("undefined.FoodProduct", on_delete=models.CASCADE)
    O_T_M_Product_OrderItems = models.ForeignKey("undefined.DrinkProduct", on_delete=models.CASCADE)

    #  Fields
    Discount = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_OrderItem_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_OrderItem_update", args=(self.pk,))


class Address(models.Model):

    #  Relationships
    O_T_M_User_Adresses = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    #  Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    AddressType = models.TextField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    DoorNumberAndOthers = models.TextField(max_length=200)
    City = models.TextField(max_length=100)
    ZipCode = models.TextField(max_length=20)
    StreetAndStreetNumber = models.TextField(max_length=200)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_Address_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_Address_update", args=(self.pk,))


class Ingredient(models.Model):

    #  Relationships
    FoodProduct_To_Ingredient = models.ManyToManyField("undefined.FoodProduct")

    #  Fields
    RemainingAmountInInventory = models.FloatField()
    FatsPerServing = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    PricePerServing = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    isTopping = models.BooleanField()
    ProteinPerServing = models.FloatField()
    IsAllergen = models.BooleanField()
    CarbsPerServing = models.FloatField()
    DairyFree = models.BooleanField()
    Vegan = models.BooleanField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_Ingredient_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_Ingredient_update", args=(self.pk,))


class Courier(models.Model):

    #  Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    Phone = models.TextField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    Name = models.TextField(max_length=100)
    GpsCoordinates = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_Courier_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_Courier_update", args=(self.pk,))


class Order(models.Model):

    #  Relationships
    O_T_O_Transaction_Order = models.OneToOneField("undefined.Transaction")
    Courier_Orders = models.ForeignKey("undefined.Courier", on_delete=models.CASCADE)
    O_T_M_User_Orders = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    #  Fields
    DeliveryDate = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    ExpectedGivingToCourierDate = models.DateTimeField()
    Status = models.TextField(max_length=30)
    GivenToCourierDate = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    Comment = models.TextField(max_length=300)
    Discount = models.FloatField()
    ExpectedDeliveryDate = models.DateTimeField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_Order_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_Order_update", args=(self.pk,))


class FoodProduct(Product):

    #  Relationships
    FoodProduct_To_Ingredient_2 = models.ManyToManyField("undefined.Ingredient")

    #  Fields
    Vegan = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    Vegetarian = models.BooleanField()
    GlutenFree = models.BooleanField()
    UserCreated = models.BooleanField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_FoodProduct_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_FoodProduct_update", args=(self.pk,))


class DrinkProduct(Product):

    #  Fields
    ContainsCaffeine = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    Calories = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    SugarContent = models.IntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_DrinkProduct_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_DrinkProduct_update", args=(self.pk,))

class UserPizza(models.Model):

    # Relationships
    O_T_O_User_UserPizza = models.OneToOneField("undefined.User")
    O_T_O_FoodProduct_UserPizza = models.OneToOneField("undefined.FoodProduct")

    # Fields
    Nickname = models.TextField(max_length=50)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_UserPizza_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_UserPizza_update", args=(self.pk,))


class User(AbstractBaseUser):

    #  Relationships
    M_T_O_PriviligeLevel_User = models.ForeignKey("undefined.PriviligeLevel", on_delete=models.CASCADE)

    #  Fields
    emailToken = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_User_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_User_update", args=(self.pk,))
