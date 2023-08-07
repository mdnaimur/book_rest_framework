from dataclasses import field
from multiprocessing import Value
from rest_framework import serializers
from book_api.models import Book
from django.forms import ValidationError


# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     title = serializers.CharField(max_length=100)
#     number_of_pages = serializers.IntegerField(default =False)
#     publish_date  =serializers.DateField()
#     quantity = serializers.IntegerField(default =False)


#     def create(self,data):
#         return Book.objects.create(**data)

#     def update(self,instance,data):
#         instance.title = data.get('title',instance.title)
#         instance.number_of_pages = data.get('number_of_pages',instance.number_of_pages)
#         instance.publish_date = data.get('publish_date',instance.publish_date)
#         instance.quantity = data.get('quantity',instance.quantity)
#         instance.title = data.get('title',instance.title)

#         instance.save()
#         return instance


class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        if value == 'naimur':
            raise ValidationError("Admin name should not used")
        return value

    def get_description(self, data):
        return "This book is called " + data.title + "and it is" + str(data.number_of_pages) + " pages long."
