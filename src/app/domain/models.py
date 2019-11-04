from django.db import models
from django.urls import reverse
from django.contrib.auth.base_user import AbstractBaseUser

# Pay extra attention for using snake_case !! Things wont work otherwise. This is Python, not Java!

class Product(models.Model):
    #  Fields
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=300)
    size = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    price = models.FloatField()
    public_product_id = models.IntegerField()

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
    M_T_M_Priviliges_Emails = models.ManyToManyField("app.PriviligeLevel")

    #  Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type = models.TextField(max_length=60)

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
    M_T_M_Priviligies_Emails2 = models.ManyToManyField(EmailTemplate)

    #  Fields
    name = models.TextField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    grants_access_to = models.TextField(max_length=100)

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
    O_T_O_Order_Transaction = models.OneToOneField("app.Order", on_delete=models.CASCADE, null = True)

    #  Fields
    payment_type = models.TextField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    was_payback = models.BooleanField()
    payment_option = models.TextField(max_length=100)
    amount = models.FloatField()
    currency = models.TextField(max_length=30)
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
    O_T_M_Order_OrderItems = models.ForeignKey("app.Order", on_delete=models.CASCADE)

    #  Fields
    discount = models.FloatField()
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
    O_T_M_User_Adresses = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE)

    #  Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    address_type = models.TextField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    door_number_and_others = models.TextField(max_length=200)
    city = models.TextField(max_length=100)
    zip_code = models.TextField(max_length=20)
    street_and_street_number = models.TextField(max_length=200)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_Address_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_Address_update", args=(self.pk,))


class Ingredient(models.Model):
    #  Fields
    remaining_amount_in_inventory = models.FloatField()
    fats_per_serving = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    price_per_serving = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    is_topping = models.BooleanField()
    protein_per_serving = models.FloatField()
    is_allergen = models.BooleanField()
    carbs_per_serving = models.FloatField()
    dairy_free = models.BooleanField()
    vegan = models.BooleanField()

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
    phone = models.TextField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.TextField(max_length=100)
    gps_coordinates = models.TextField(max_length=100)

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
    Courier_Orders = models.ForeignKey(Courier, on_delete=models.CASCADE)
    O_T_M_User_Orders = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    O_T_O_Address_Order = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    #  Fields
    delivery_date = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    expected_giving_to_courier_date = models.DateTimeField()
    status = models.TextField(max_length=30)
    given_to_courier_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    comment = models.TextField(max_length=300)
    discount = models.FloatField()
    expected_delivery_date = models.DateTimeField()

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
    FoodProduct_To_Ingredient_2 = models.ManyToManyField(Ingredient)
    O_T_M_OrderItem_FoodProducts = models.ForeignKey("app.OrderItem", on_delete=models.CASCADE, null = True)

    #  Fields
    vegan = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    vegetarian = models.BooleanField()
    gluten_free = models.BooleanField()
    user_created = models.BooleanField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("PizzaDeliverySystem_FoodProduct_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("PizzaDeliverySystem_FoodProduct_update", args=(self.pk,))


class DrinkProduct(Product):
    # Relationships
    O_T_M_OrderItem_DrinkProducts = models.ForeignKey("app.OrderItem", on_delete=models.CASCADE, null = True)
    #  Fields
    contains_caffeine = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    calories = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    sugar_content = models.IntegerField()

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
    O_T_O_User_UserPizza = models.OneToOneField("app.User", on_delete=models.CASCADE)
    O_T_O_FoodProduct_UserPizza = models.OneToOneField(FoodProduct, on_delete=models.CASCADE)

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
    M_T_O_PriviligeLevel_User = models.ForeignKey(PriviligeLevel, on_delete=models.CASCADE)

    #  Fields
    email_token = models.TextField(max_length=200)
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
