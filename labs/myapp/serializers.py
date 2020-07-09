from rest_framework import serializers
from myapp.models import User, ActivityPeriod

#ActivityPeriod serializer
class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = '__all__'

#User Serializer
class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True, read_only=False)

    class Meta:
        model = User
        fields = [ 
            "id",
            "real_name",
            "tz",
            "activity_periods"
        ]
    
    def create(self, validated_data):
        choice_validated_data = validated_data.pop('activity_periods')
        user = User.objects.create(**validated_data)
        choice_set_serializer = self.fields['activity_periods']
        for each in choice_validated_data:
            each['user'] = user
        choices = choice_set_serializer.create(choice_validated_data)
        return user



