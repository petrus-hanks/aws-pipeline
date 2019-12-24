from django.db import models


class User(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	email = models.EmailField(primary_key=True)
	password = models.CharField(max_length=128)

	class Meta:
		ordering = ['created']


class CompanyInfo(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	email = models.EmailField(primary_key=True)
	company_name = models.CharField(max_length=130, default=" ")
	contact = models.CharField(max_length=30, default=" ")
	phone_number = models.CharField(max_length=20, default=" ")

	CHINA = 'CH'
	GLOBAL = 'GL'
	ACCOUNT_TYPE = [
		(CHINA, 'China'),
		(GLOBAL, 'Global')]
	account_type = models.CharField(
		max_length=2,
		choices=ACCOUNT_TYPE,
		default=CHINA,
	)
	account_id = models.CharField(max_length=30)
	address = models.TextField(default=" ")
	company_url = models.URLField(blank=True)
	postal_code = models.CharField(max_length=10, default=" ")

	business_plan = models.URLField(default=" ")
	license = models.URLField(default=" ")
	agreement = models.URLField(default=" ")

	class Meta:
		ordering = ['created']
