from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('rewardcustomers/', views.rewardcustomer_list, name='rewardcustomer_list'),
    path('rewardcustomers/create/', views.rewardcustomer_create, name='rewardcustomer_create'),
    path('rewardcustomers/<int:pk>/edit/', views.rewardcustomer_edit, name='rewardcustomer_edit'),
    path('rewardcustomers/<int:pk>/delete/', views.rewardcustomer_delete, name='rewardcustomer_delete'),
    path('rewards/', views.reward_list, name='reward_list'),
    path('rewards/create/', views.reward_create, name='reward_create'),
    path('rewards/<int:pk>/edit/', views.reward_edit, name='reward_edit'),
    path('rewards/<int:pk>/delete/', views.reward_delete, name='reward_delete'),
    path('pointtransactions/', views.pointtransaction_list, name='pointtransaction_list'),
    path('pointtransactions/create/', views.pointtransaction_create, name='pointtransaction_create'),
    path('pointtransactions/<int:pk>/edit/', views.pointtransaction_edit, name='pointtransaction_edit'),
    path('pointtransactions/<int:pk>/delete/', views.pointtransaction_delete, name='pointtransaction_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
