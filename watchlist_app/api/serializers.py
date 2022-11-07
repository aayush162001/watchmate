from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform



class WatchSerilizer(serializers.ModelSerializer):
    
    
    class Meta:
        model = WatchList
        fields = "__all__"
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"            


# class MoiveSerilizer(serializers.ModelSerializer):
    
#     len_name = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Movie
#         fields = "__all__"
        
#     def get_len_name(self, object):
#         return len(object.name)
    
#     def validate_name(self,values):
#         if len(values) < 2:
#             raise serializers.ValidationError("Name is too short")
#         else:
#             return values
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(" Name and Description are same")
#         else:
#             return data
    # class Meta:
    #     model = Movie
        # fields = ['id','name','description']
        # exclude = ['active']

# def name_lenght(value):
#     if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
    

# class MoiveSerilizer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validator = [name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     # def validate_name(self,values):
#     #     if len(values) < 2:
#     #         raise serializers.ValidationError("Name is too short")
#     #     else:
#     #         return values
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(" Name and Description are same")
#         else:
#             return data