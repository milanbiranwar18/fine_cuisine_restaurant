from rest_framework import serializers
from menu.models import MenuCategory, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    menu_category = serializers.CharField(max_length=100)

    class Meta:
        model = MenuItem
        fields = ['id', 'item_name', 'description', 'price', 'menu_category']
        read_only_fields = ['menu_category']

    def create(self, validated_data):
        user = self.context.get('user')
        name = validated_data.get('menu_category')
        menu_category_list = MenuCategory.objects.filter(user_id=user.id, name=name)
        if len(menu_category_list) == 0:
            menu_category = MenuCategory.objects.create(user_id=user.id, name=name)
        else:
            menu_category = menu_category_list.first()
        menu_item_list = MenuItem.objects.filter(menu_category_id=menu_category.id)
        # category_name = validated_data.pop('category')
        validated_data.pop('menu_category')
        if len(menu_item_list) == 0:
            menu_item = MenuItem.objects.create(menu_category_id=menu_category.id, **validated_data)
        else:
            menu_item = menu_item_list.first()

        return menu_item


class MenuCategorySerializer(serializers.ModelSerializer):
    # cart_items = serializers.SerializerMethodField('get_cart_items', read_only=True)

    # def get_cart_items(self, cart):
    #     items = cart.cart_items.filter(cart_id=cart.id)
    #     data = [{"book_id": x.id, "quantity": x.quantity} for x in items]
    #     return data


    class Meta:
        model = MenuCategory
        fields = ['id', 'name', "user"]
