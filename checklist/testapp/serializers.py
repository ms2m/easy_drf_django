from rest_framework import serializers
from testapp.models import SecuredList

# class CheckListSeralizer(serializers.Serializer):
#     title = serializers.CharField()
#     is_deleted = serializers.BooleanField()
#     is_archived = serializers.BooleanField()
#     created_on = serializers.DateTimeField()
#     updated_on = serializers.DateTimeField()


class SecuredListSeralizer(serializers.ModelSerializer):
    # user value will be saved the current users who is logged in.
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = SecuredList
        fields = '__all__'
