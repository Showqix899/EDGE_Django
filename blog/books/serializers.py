
#### rest framework
from rest_framework import serializers


### django 
from datetime import datetime, timedelta
from django.utils import timezone


#######
from .models import Book,Author,Publisher



#serializing the Authon  model

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields='__all__'



#serializing the Publisher model
class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields='__all__'



#serializing the book model
class BookSerializer(serializers.ModelSerializer):


    author=AuthorSerializer()
    publisher=PublisherSerializer()


    class Meta:
        model = Book
        fields = '__all__' 


    #adding custom validation
    def validate(self, attrs):

        #title must be  at least 80 characters long

        if attrs.get('title') and len(attrs['title'])> 80:
            raise  serializers.ValidationError('title can not be greater then 80 charecter')
    
        #description must be less then 10 words
        if attrs.get('description'):
            description_word_count = len(attrs['description'].split())
            if description_word_count > 10:
                raise serializers.ValidationError('Description cannot be greater than 10 words.')

        # Validate publication date (must be at least 1 month old)
        if attrs.get('publication_date'):
            one_month_ago = datetime.now().date() - timedelta(days=30)
            if attrs['publication_date'] > one_month_ago:
                raise serializers.ValidationError('Publication date must be at least 1 month old.')
        
        #validating price between 100  to 10000
        if attrs.get('price') and attrs['price']< 100 and attrs['price']>10000:
            raise serializers.ValidationError('price must be between 100 to 10000')
        

        return attrs

        #custom create method for  creating book instance

    def create(self, validated_data):

        #for author
        author=validated_data.pop('author')
        author_serializer=AuthorSerializer(data=author)

        if  author_serializer.is_valid():
            author_instance=author_serializer.save()
            validated_data['author']=author_instance

        #for publisher

        publisher=validated_data.pop('publisher')
        publisher_serializer=PublisherSerializer(data=publisher)

        if publisher_serializer.is_valid():
            publisher_instance=publisher_serializer.save()
            validated_data['publisher']=publisher_instance


        return super().create(validated_data) 

    def update(self, instance, validated_data):
        validated_data['updated_at']=timezone.now()
        return super().update(instance, validated_data) 



