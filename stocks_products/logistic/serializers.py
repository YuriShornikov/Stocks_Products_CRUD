from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'description']



class ProductPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockProduct
        fields = ['product', 'price', 'quantity']



class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']


    def create(self, validated_data):

        positions = validated_data.pop('positions')

        stock = super().create(validated_data)
        for position in positions:
            StockProduct.objects.get_or_create(stock=stock, **position)

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)


        for position in positions:
            current_product = StockProduct.objects.filter(stock=stock, product=position['product'])
            if current_product.exists():
                StockProduct.objects.filter(stock=stock, product=position['product']).update(**position)
            else:
                StockProduct.objects.create(stock=stock, **position)
        return stock
