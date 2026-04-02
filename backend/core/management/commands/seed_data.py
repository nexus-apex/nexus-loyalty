from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import RewardCustomer, Reward, PointTransaction
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusLoyalty with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusloyalty.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if RewardCustomer.objects.count() == 0:
            for i in range(10):
                RewardCustomer.objects.create(
                    name=f"Sample RewardCustomer {i+1}",
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    points_balance=random.randint(1, 100),
                    tier=random.choice(["bronze", "silver", "gold", "platinum"]),
                    total_earned=random.randint(1, 100),
                    total_redeemed=random.randint(1, 100),
                    joined_date=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 RewardCustomer records created'))

        if Reward.objects.count() == 0:
            for i in range(10):
                Reward.objects.create(
                    name=f"Sample Reward {i+1}",
                    points_required=random.randint(1, 100),
                    category=random.choice(["discount", "freebie", "cashback", "experience"]),
                    stock=random.randint(1, 100),
                    status=random.choice(["active", "out_of_stock", "expired"]),
                    redeemed_count=random.randint(1, 100),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Reward records created'))

        if PointTransaction.objects.count() == 0:
            for i in range(10):
                PointTransaction.objects.create(
                    customer_name=f"Sample PointTransaction {i+1}",
                    points=random.randint(1, 100),
                    transaction_type=random.choice(["earned", "redeemed", "expired", "bonus"]),
                    reference=f"Sample {i+1}",
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 PointTransaction records created'))
