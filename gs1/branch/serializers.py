from rest_framework import serializers
class BranchSerializer(serializers.Serializer):
 id = serializers.IntegerField()
 name = serializers.CharField(max_length=100)
 roll = serializers.IntegerField()
 branch = serializers.CharField(max_length=100)