from django.db import models

class RewardCustomer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    points_balance = models.IntegerField(default=0)
    tier = models.CharField(max_length=50, choices=[("bronze", "Bronze"), ("silver", "Silver"), ("gold", "Gold"), ("platinum", "Platinum")], default="bronze")
    total_earned = models.IntegerField(default=0)
    total_redeemed = models.IntegerField(default=0)
    joined_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Reward(models.Model):
    name = models.CharField(max_length=255)
    points_required = models.IntegerField(default=0)
    category = models.CharField(max_length=50, choices=[("discount", "Discount"), ("freebie", "Freebie"), ("cashback", "Cashback"), ("experience", "Experience")], default="discount")
    stock = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("out_of_stock", "Out of Stock"), ("expired", "Expired")], default="active")
    redeemed_count = models.IntegerField(default=0)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class PointTransaction(models.Model):
    customer_name = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    transaction_type = models.CharField(max_length=50, choices=[("earned", "Earned"), ("redeemed", "Redeemed"), ("expired", "Expired"), ("bonus", "Bonus")], default="earned")
    reference = models.CharField(max_length=255, blank=True, default="")
    date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.customer_name
