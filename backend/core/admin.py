from django.contrib import admin
from .models import RewardCustomer, Reward, PointTransaction

@admin.register(RewardCustomer)
class RewardCustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "points_balance", "tier", "created_at"]
    list_filter = ["tier"]
    search_fields = ["name", "email", "phone"]

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ["name", "points_required", "category", "stock", "status", "created_at"]
    list_filter = ["category", "status"]
    search_fields = ["name"]

@admin.register(PointTransaction)
class PointTransactionAdmin(admin.ModelAdmin):
    list_display = ["customer_name", "points", "transaction_type", "reference", "date", "created_at"]
    list_filter = ["transaction_type"]
    search_fields = ["customer_name", "reference"]
