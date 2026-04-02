import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import RewardCustomer, Reward, PointTransaction


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['rewardcustomer_count'] = RewardCustomer.objects.count()
    ctx['rewardcustomer_bronze'] = RewardCustomer.objects.filter(tier='bronze').count()
    ctx['rewardcustomer_silver'] = RewardCustomer.objects.filter(tier='silver').count()
    ctx['rewardcustomer_gold'] = RewardCustomer.objects.filter(tier='gold').count()
    ctx['reward_count'] = Reward.objects.count()
    ctx['reward_discount'] = Reward.objects.filter(category='discount').count()
    ctx['reward_freebie'] = Reward.objects.filter(category='freebie').count()
    ctx['reward_cashback'] = Reward.objects.filter(category='cashback').count()
    ctx['pointtransaction_count'] = PointTransaction.objects.count()
    ctx['pointtransaction_earned'] = PointTransaction.objects.filter(transaction_type='earned').count()
    ctx['pointtransaction_redeemed'] = PointTransaction.objects.filter(transaction_type='redeemed').count()
    ctx['pointtransaction_expired'] = PointTransaction.objects.filter(transaction_type='expired').count()
    ctx['recent'] = RewardCustomer.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def rewardcustomer_list(request):
    qs = RewardCustomer.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(tier=status_filter)
    return render(request, 'rewardcustomer_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def rewardcustomer_create(request):
    if request.method == 'POST':
        obj = RewardCustomer()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.points_balance = request.POST.get('points_balance') or 0
        obj.tier = request.POST.get('tier', '')
        obj.total_earned = request.POST.get('total_earned') or 0
        obj.total_redeemed = request.POST.get('total_redeemed') or 0
        obj.joined_date = request.POST.get('joined_date') or None
        obj.save()
        return redirect('/rewardcustomers/')
    return render(request, 'rewardcustomer_form.html', {'editing': False})


@login_required
def rewardcustomer_edit(request, pk):
    obj = get_object_or_404(RewardCustomer, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.points_balance = request.POST.get('points_balance') or 0
        obj.tier = request.POST.get('tier', '')
        obj.total_earned = request.POST.get('total_earned') or 0
        obj.total_redeemed = request.POST.get('total_redeemed') or 0
        obj.joined_date = request.POST.get('joined_date') or None
        obj.save()
        return redirect('/rewardcustomers/')
    return render(request, 'rewardcustomer_form.html', {'record': obj, 'editing': True})


@login_required
def rewardcustomer_delete(request, pk):
    obj = get_object_or_404(RewardCustomer, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/rewardcustomers/')


@login_required
def reward_list(request):
    qs = Reward.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(category=status_filter)
    return render(request, 'reward_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def reward_create(request):
    if request.method == 'POST':
        obj = Reward()
        obj.name = request.POST.get('name', '')
        obj.points_required = request.POST.get('points_required') or 0
        obj.category = request.POST.get('category', '')
        obj.stock = request.POST.get('stock') or 0
        obj.status = request.POST.get('status', '')
        obj.redeemed_count = request.POST.get('redeemed_count') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/rewards/')
    return render(request, 'reward_form.html', {'editing': False})


@login_required
def reward_edit(request, pk):
    obj = get_object_or_404(Reward, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.points_required = request.POST.get('points_required') or 0
        obj.category = request.POST.get('category', '')
        obj.stock = request.POST.get('stock') or 0
        obj.status = request.POST.get('status', '')
        obj.redeemed_count = request.POST.get('redeemed_count') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/rewards/')
    return render(request, 'reward_form.html', {'record': obj, 'editing': True})


@login_required
def reward_delete(request, pk):
    obj = get_object_or_404(Reward, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/rewards/')


@login_required
def pointtransaction_list(request):
    qs = PointTransaction.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(customer_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(transaction_type=status_filter)
    return render(request, 'pointtransaction_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def pointtransaction_create(request):
    if request.method == 'POST':
        obj = PointTransaction()
        obj.customer_name = request.POST.get('customer_name', '')
        obj.points = request.POST.get('points') or 0
        obj.transaction_type = request.POST.get('transaction_type', '')
        obj.reference = request.POST.get('reference', '')
        obj.date = request.POST.get('date') or None
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/pointtransactions/')
    return render(request, 'pointtransaction_form.html', {'editing': False})


@login_required
def pointtransaction_edit(request, pk):
    obj = get_object_or_404(PointTransaction, pk=pk)
    if request.method == 'POST':
        obj.customer_name = request.POST.get('customer_name', '')
        obj.points = request.POST.get('points') or 0
        obj.transaction_type = request.POST.get('transaction_type', '')
        obj.reference = request.POST.get('reference', '')
        obj.date = request.POST.get('date') or None
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/pointtransactions/')
    return render(request, 'pointtransaction_form.html', {'record': obj, 'editing': True})


@login_required
def pointtransaction_delete(request, pk):
    obj = get_object_or_404(PointTransaction, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/pointtransactions/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['rewardcustomer_count'] = RewardCustomer.objects.count()
    data['reward_count'] = Reward.objects.count()
    data['pointtransaction_count'] = PointTransaction.objects.count()
    return JsonResponse(data)
