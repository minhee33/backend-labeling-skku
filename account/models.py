from django.db import models

class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length = 50, unique = True)
    password = models.CharField(max_length= 200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'account'

class Label(models.Model):
    id = models.BigAutoField(help_text="Label ID", primary_key=True)
    account = models.ForeignKey("Account", related_name="account", on_delete=models.CASCADE, db_column="account_id")
    name = models.CharField(max_length= 200, default="")
    color_code = models.CharField(max_length= 100, default="#171718")

    class Meta:
        db_table = 'label'