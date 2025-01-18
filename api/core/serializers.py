from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError
from datetime import datetime


class ClassSerializer(serializers.ModelSerializer):
    days = serializers.MultipleChoiceField(
        choices=Class.DAYS_OF_WEEK,
        required=True,
        label="Days of the Week"
    )

    times = serializers.CharField(
        required=True,
        label="Class Times (comma-separated HH:MM:SS)"
    )

    class Meta:
        model = Class
        fields = '__all__'

    def validate_times(self, value):
        times_list = [t.strip() for t in value.split(',')]
        validated_times = []
        for time in times_list:
            try:
                validated_times.append(datetime.strptime(time, '%H:%M:%S').time())
            except ValueError:
                raise serializers.ValidationError("Each time must be in HH:MM:SS format.")
        return validated_times

    def validate(self, data):
        days = data.get('days', [])
        times = data.get('times', [])
        if len(days) != len(times):
            raise serializers.ValidationError("The number of days must match the number of times.")
        return data


class StatusSerializer(serializers.ModelSerializer):
    expected = serializers.CharField(
        required=True,
        label="Expected Times (comma-separated HH:MM:SS)"
    )

    register = serializers.CharField(
        required=True,
        label="Register Times (comma-separated HH:MM:SS)"
    )

    class Meta:
        model = Status
        fields = '__all__'

    def check_times(self, typ):
        times = self.initial_data.get(typ)
        if not times:
            return []
        times_list = [t.strip() for t in times.split(',')]
        validated_times = []
        for time in times_list:
            try:
                validated_times.append(datetime.strptime(time, '%H:%M:%S').time())
            except ValueError:
                raise serializers.ValidationError("Each time must be in HH:MM:SS format.")
        return validated_times

    def validate_expected(self, value):
        return self.check_times('expected')

    def validate_register(self, value):
        return self.check_times('register')

    def validate(self, data):
        expected = data.get('expected', [])
        register = data.get('register', [])
        if len(expected) != len(register):
            raise serializers.ValidationError("The number of expected times must match the number of register times.")
        return data


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    STATUS = [
        ('sent', 'SENT'),
        ('awaiting', 'AWAITING')
    ]

    message = serializers.PrimaryKeyRelatedField(queryset=Message.objects.all(), required=True)
    status = serializers.ChoiceField(choices=STATUS, required=True)
    created_at = serializers.DateTimeField(required=True)
    destination = serializers.DateTimeField(required=True)
    classy = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), required=False)
    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)

    class Meta:
        model = Notification
        fields = '__all__'
