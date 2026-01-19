from django.db import models

class Account(models.Model):
    account_no = models.CharField(max_length=20, unique=True, primary_key=True, db_column='accountno') # Matches existing schema roughly, strict mapping might trigger migration
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    pin = models.IntegerField()
    email = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)

    class Meta:
        db_table = 'accounts' # OPTIONAL: To map to the existing table we manually created. 
        # If we want Django to manage it, we might need a fake migration or just let it sync.
        # Given we created the table manually with specific columns, using db_table='accounts' is good to reuse data.

    def __str__(self):
        return f"{self.name} ({self.account_no})"
