from rest_framework import serializers
from pipeline.models import CompanyInfo, User


class WhiteListSerializer(serializers.ModelSerializer):
	class Meta:
		model = CompanyInfo
		fields = [
			'email',
			'company_name',
			'contact',
			'phone_number'
		]


class CreditSerializer(serializers.ModelSerializer):
	class Meta:
		model = CompanyInfo
		fields = [
			'email',
			'account_type',
			'account_id',
			'address',
			'company_url',
			'postal_code',
			'business_plan',
			'license',
			'agreement'
		]


class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = [
			'email',
			'password'
		]