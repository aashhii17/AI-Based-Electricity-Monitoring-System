from django.urls import path
from . import views
from . import views_test
from . import views_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Authentication routes
    path('signup/', views.signup_view, name='signup'),
    path('signup/add_appliances/', views.add_appliances_view, name='signup_add_appliances'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.user_login),  # Default home route redirects to login
    path('register/', views.register_user, name='register'),

    # User dashboard and appliance routes
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add_appliances/', views.add_appliances_view, name='add_appliances'),
    path('add_appliances', views.add_appliances_view, name='add_appliances_no_slash'),  # optional route without slash
    path('add-appliance/', views.add_appliances_view, name='add_appliance_redirect'),
    path('appliances/', views.appliances_list_view, name='appliances_list'),
    path('consumption/<int:appliance_id>/', views.consumption_view, name='consumption'),
    path('predictions/', views.predictions_view, name='predictions'),
    path('generate_predictions/', views.generate_predictions_view, name='generate_predictions'),
    path('reports/', views.reports_view, name='reports'),

    # Admin dashboard
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('admin_dashboard/export/', views.export_user_data_to_excel, name='export_user_data'),

    path('profile/', views_profile.profile_view, name='profile'),
    path('delete_account/', views_profile.delete_account_view, name='delete_account'),
    path('delete-account/', views_profile.delete_account_view, name='delete_account_redirect'),
    path('switch_account/', views_profile.switch_account_view, name='switch_account'),
    path('switch-account/', views_profile.switch_account_view, name='switch_account_redirect'),

    # Test route
    path('test_admin_dashboard/', views_test.test_admin_dashboard, name='test_admin_dashboard'),

    path('remove_appliance/<int:appliance_id>/', views.remove_appliance_view, name='remove_appliance'),
    path('admin_remove_appliance/<int:appliance_id>/', views.admin_remove_appliance_view, name='admin_remove_appliance'),
    path('admin_add_appliance/', views.admin_add_appliance_view, name='admin_add_appliance'),
    path('admin_remove_user/<int:user_profile_id>/', views.admin_remove_user_view, name='admin_remove_user'),
]

# Static file serving during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR.parent / 'Templates' / 'static')
