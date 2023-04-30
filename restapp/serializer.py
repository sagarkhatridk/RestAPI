from rest_framework import serializers
import re
from .models import ToDo, TimingTodo
from django.template.defaultfilters import slugify


class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = ToDo
        fields = ['uid', 'Todo_Title', 'slug', 'Todo_Description', 'is_Done']

        # similar as fields
        # exclude will remove filds you have given
        # exclude = ['created_at', 'updated_at']

    def get_slug(self, obj):

        return slugify(obj.Todo_Title)

    def validate_todo_title(self, data):

        if data:
            Todo_Title = data

            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

            if not regex.search(Todo_Title) is None:
                raise serializers.ValidationError("Todo title can not contains special characters")

        return data

class TodoTimingSerializer(serializers.ModelSerializer):
    todo = TodoSerializer()

    class Meta:
        model = TimingTodo
        exclude = ['created_at', 'updated_at']
