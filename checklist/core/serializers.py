from rest_framework import serializers

from core.models import CheckList, CheckListItem

# class CheckListSeralizer(serializers.Serializer):
#     title = serializers.CharField()
#     is_deleted = serializers.BooleanField()
#     is_archived = serializers.BooleanField()
#     created_on = serializers.DateTimeField()
#     updated_on = serializers.DateTimeField()


class CheckListSeralizer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = '__all__'

class CheckListItemSeralizer(serializers.ModelSerializer):
    class Meta:
        model = CheckListItem
        fields = '__all__'
