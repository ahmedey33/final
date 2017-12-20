from rest_framework import serializers
from .models import HobbyCat, HobbyItem

class HobbyCatSerializer(serializers.ModelSerializer):

	class Meta:
		model = HobbyCat
		fields = '__all__'

		# If all field are required
		# fields = '__all__'

class HobbyItemtSerializer(serializers.ModelSerializer):

	class Meta:
		model = HobbyItem
		fields = '__all__'