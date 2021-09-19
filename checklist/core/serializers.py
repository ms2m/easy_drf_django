from rest_framework import serializers

from core.models import CheckList, CheckListItem

# class CheckListSeralizer(serializers.Serializer):
#     title = serializers.CharField()
#     is_deleted = serializers.BooleanField()
#     is_archived = serializers.BooleanField()
#     created_on = serializers.DateTimeField()
#     updated_on = serializers.DateTimeField()


class CheckListItemSeralizer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CheckListItem
        fields = '__all__'


class CheckListSeralizer(serializers.ModelSerializer):
    items = CheckListItemSeralizer(source='checklistitem_set', many=True, read_only=True)
    # user value will be saved the current users who is logged in.
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CheckList
        fields = '__all__'
