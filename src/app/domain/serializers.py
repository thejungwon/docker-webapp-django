from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = [
            "Name",
            "Description",
            "Size",
            "last_updated",
            "created",
            "Price",
            "PublicProductId",
        ]

class EmailTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EmailTemplate
        fields = [
            "created",
            "last_updated",
            "Type",
        ]

class PriviligeLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PriviligeLevel
        fields = [
            "Name",
            "created",
            "last_updated",
            "GrantsAccessTo",
        ]

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transaction
        fields = [
            "PaymentType",
            "last_updated",
            "WasPayback",
            "PaymentOption",
            "Amount",
            "Currency",
            "created",
        ]

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderItem
        fields = [
            "Discount",
            "created",
            "last_updated",
        ]

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Address
        fields = [
            "last_updated",
            "AddressType",
            "created",
            "DoorNumberAndOthers",
            "City",
            "ZipCode",
            "StreetAndStreetNumber",
        ]

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ingredient
        fields = [
            "RemainingAmountInInventory",
            "FatsPerServing",
            "last_updated",
            "PricePerServing",
            "created",
            "isTopping",
            "ProteinPerServing",
            "IsAllergen",
            "CarbsPerServing",
            "DairyFree",
            "Vegan",
        ]

class CourierSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Courier
        fields = [
            "created",
            "Phone",
            "last_updated",
            "Name",
            "GpsCoordinates",
        ]

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = [
            "DeliveryDate",
            "last_updated",
            "ExpectedGivingToCourierDate",
            "Status",
            "GivenToCourierDate",
            "created",
            "Comment",
            "Discount",
            "ExpectedDeliveryDate",
        ]

class FoodProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FoodProduct
        fields = [
            "Vegan",
            "last_updated",
            "created",
            "Vegetarian",
            "GlutenFree",
            "UserCreated",
        ]

class DrinkProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DrinkProduct
        fields = [
            "ContainsCaffeine",
            "last_updated",
            "Calories",
            "created",
            "SugarContent",
        ]
		
class UserPizzaSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.UserPizza
		fields = [
			"Nickname",
		]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            "emailToken",
            "created",
            "last_updated",
        ]
