from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from .views.common import DirectTemplateView


guid_pattern = r'(?P<guid>[a-zA-Z0-9\-]+)'

urlpatterns = patterns('perma.views',

    # Common Pages
    url(r'^$', DirectTemplateView.as_view(template_name='landing.html', extra_context={'this_page':'landing'}), name='landing'),
    url(r'^tools/?$', DirectTemplateView.as_view(template_name='tools.html'), name='tools'),
    url(r'^about/?$', DirectTemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^additional-resources/?$', DirectTemplateView.as_view(template_name='additional-resources.html'), name='additional_resources'),
    url(r'^faq/?$', DirectTemplateView.as_view(template_name='faq.html'), name='faq'),
    url(r'^copyright-policy/?$', DirectTemplateView.as_view(template_name='copyright_policy.html'), name='copyright_policy'),
    url(r'^terms-of-service/?$', DirectTemplateView.as_view(template_name='terms_of_service.html'), name='terms_of_service'),
    url(r'^privacy-policy/?$', DirectTemplateView.as_view(template_name='privacy_policy.html'), name='privacy_policy'),
    url(r'^stats/?$', 'common.stats', name='global_stats'),
    url(r'^contingency-plan/?$', DirectTemplateView.as_view(template_name='contingency_plan.html'), name='contingency_plan'),
    url(r'^contact/?$', 'common.contact', name='contact'),
    url(r'^contact/thanks/?$', DirectTemplateView.as_view(template_name='contact-thanks.html'), name='contact_thanks'),
    
    #Docs 
    url(r'^docs/?$', DirectTemplateView.as_view(template_name='docs/index.html'), name='docs'),
    url(r'^docs/perma-link-creation/?$', DirectTemplateView.as_view(template_name='docs/perma-link-creation.html'), name='docs_perma_link_creation'),
    url(r'^docs/perma-link-vesting/?$', DirectTemplateView.as_view(template_name='docs/perma-link-vesting.html'), name='docs_perma_link_vesting'),
    url(r'^docs/perma-archive/?$', DirectTemplateView.as_view(template_name='docs/perma-archive.html'), name='docs_perma_archive'),
    url(r'^docs/libraries/?$', DirectTemplateView.as_view(template_name='docs/libraries.html'), name='docs_libraries'),
    url(r'^docs/perma-dark-archive/?$', DirectTemplateView.as_view(template_name='docs/perma-dark-archive.html'), name='docs_perma_dark_archive'),
    url(r'^docs/copyright/?$', DirectTemplateView.as_view(template_name='docs/copyright.html'), name='docs_copyright'),
    url(r'^docs/getting-started/?$', DirectTemplateView.as_view(template_name='docs/getting-started.html'), name='docs_getting-started'),
    url(r'^docs/mirrors/?$', DirectTemplateView.as_view(template_name='docs/mirrors.html'), name='docs_mirrors'),
    url(r'^docs/robustness/?$', DirectTemplateView.as_view(template_name='docs/robustness.html'), name='docs_robustness'),
    url(r'^docs/perma-user-roles/?$', DirectTemplateView.as_view(template_name='docs/perma-user-roles.html'), name='docs_perma_user_roles'),
    url(r'^docs/faq/?$', DirectTemplateView.as_view(template_name='docs/faq.html'), name='docs_faq'),

    #API routes
    url(r'^api/linky/urldump/?$', 'api.urldump', name='urldump'),
    url(r'^api/linky/urldump/(?P<since>\d{4}-\d{2}-\d{2})/?', 'api.urldump', name='urldump_with_since'),
    
    #Services
    url(r'^service/email-confirm/?$', 'service.email_confirm', name='service_email_confirm'),
    url(r'^service/receive-feedback/?$', 'service.receive_feedback', name='service_receive_feedback'),
    url(r'^service/link/status/%s?/?$' % guid_pattern, 'service.link_status', name='service_link_status'),
    url(r'^service/stats/users/?$', 'service.stats_users', name='service_stats_users'),
    url(r'^service/stats/links/?$', 'service.stats_links', name='service_stats_links'),
    url(r'^service/stats/darchive-links/?$', 'service.stats_darchive_links', name='service_stats_darchive_links'),
    url(r'^service/stats/storage/?$', 'service.stats_storage', name='service_stats_storage'),
    url(r'^service/stats/vesting-org/?$', 'service.stats_vesting_org', name='service_stats_vesting_org'),
    url(r'^service/stats/registrar/?$', 'service.stats_registrar', name='service_stats_registrar'),
    url(r'^service/bookmarklet-create/$', 'service.bookmarklet_create', name='service.bookmarklet_create'),
    url(r'^service/image-wrapper/%s?/?$' % guid_pattern, 'service.image_wrapper', name='service_image_wrapper'),

    # Session/account management
    url(r'^login/?$', 'user_management.limited_login', {'template_name': 'registration/login.html'}, name='user_management_limited_login'),
    url(r'^login/not-active/?$', 'user_management.not_active', name='user_management_not_active'),
    url(r'^login/account-is-deactivated/?$', 'user_management.account_is_deactivated', name='user_management_account_is_deactivated'),
    url(r'^logout/?$', 'user_management.logout', name='logout'),
    url(r'^register/?$', 'user_management.register', name='register'),
    #url(r'^register/confirm/(?P<code>\w+)/$', 'user_management.register_email_code_confirmation', name='confirm_register'),
    url(r'^register/password/(?P<code>\w+)/$', 'user_management.register_email_code_password', name='register_password'),
    url(r'^register/email/?$', 'user_management.register_email_instructions', name='register_email_instructions'),
    url(r'^password/change/?$', auth_views.password_change, {'template_name': 'registration/password_change_form.html'}, name='password_change'),
    url(r'^password/change/done/?$', auth_views.password_change_done, {'template_name': 'registration/password_change_done.html'},   name='password_change_done'),
    url(r'^password/reset/?$', auth_views.password_reset, {'template_name': 'registration/password_reset_form.html'}, name='password_reset'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^password/reset/complete/?$', auth_views.password_reset_complete, {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^password/reset/done/?$', auth_views.password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^manage/account/?$', 'user_management.manage_account', name='user_management_manage_account'),
    
    # Link management
    url(r'^manage/?$', RedirectView.as_view(url='/manage/create/', permanent=False)),
    url(r'^manage/create/?$', 'link_management.create_link', name='create_link'),
    url(r'^manage/create/upload/?$', 'link_management.upload_file', name='upload_link'),
    url(r'^manage/dark-archive/%s/?$' % guid_pattern, 'link_management.dark_archive_link', name='dark_archive_link'),
    url(r'^manage/vest/%s/?$' % guid_pattern, 'link_management.vest_link', name='vest_link'),
    url(r'^manage/delete-link/%s/?$' % guid_pattern, 'link_management.user_delete_link', name='user_delete_link'),
    url(r'^manage/links/folder/(?P<folder_id>.+?)/?$', 'link_management.folder_contents', name='folder_contents'),
    url(r'^manage/links(?P<path>/.*)?$', 'link_management.link_browser', name='link_browser'),

    # user management
    url(r'^manage/registrars/?$', 'user_management.manage_registrar', name='user_management_manage_registrar'),
    url(r'^manage/registrars/(?P<registrar_id>[a-zA-Z0-9]+)/?$', 'user_management.manage_single_registrar', name='user_management_manage_single_registrar'),
    url(r'^manage/vesting-organizations/?$', 'user_management.manage_vesting_org', name='user_management_manage_vesting_org'),
    url(r'^manage/vesting-organizations/(?P<vesting_org_id>[a-zA-Z0-9]+)/?$', 'user_management.manage_single_vesting_org', name='user_management_manage_single_vesting_org'),
    url(r'^manage/registrar-users/?$', 'user_management.manage_registrar_user', name='user_management_manage_registrar_user'),
    url(r'^manage/registrar-users/(?P<user_id>[a-zA-Z0-9]+)/?$', 'user_management.manage_single_registrar_user', name='user_management_manage_single_registrar_user'),
    url(r'^manage/registrar-user/(?P<user_id>[a-zA-Z0-9]+)/delete/?$', 'user_management.manage_single_registrar_user_delete', name='user_management_manage_single_registrar_user_delete'),
    url(r'^manage/registrar-users/(?P<user_id>[a-zA-Z0-9]+)/reactivate/?$', 'user_management.manage_single_registrar_user_reactivate', name='user_management_manage_single_registrar_user_reactivate'),
    url(r'^manage/users/?$', 'user_management.manage_user', name='user_management_manage_user'),
    url(r'^manage/users/(?P<user_id>[a-zA-Z0-9]+)/?$', 'user_management.manage_single_user', name='user_management_manage_single_user'),
    url(r'^manage/users/(?P<user_id>[a-zA-Z0-9]+)/delete/?$', 'user_management.manage_single_user_delete', name='user_management_manage_single_user_delete'),
    url(r'^manage/users/(?P<user_id>[a-zA-Z0-9]+)/reactivate/?$', 'user_management.manage_single_user_reactivate', name='user_management_manage_single_user_reactivate'),
    url(r'^manage/vesting-users/?$', 'user_management.manage_vesting_user', name='user_management_manage_vesting_user'),
    url(r'^manage/vesting-users/(?P<user_id>[a-zA-Z0-9]+)/?$', 'user_management.manage_single_vesting_user', name='user_management_manage_single_vesting_user'),
    url(r'^manage/vesting-users/(?P<user_id>[a-zA-Z0-9]+)/delete/?$', 'user_management.manage_single_vesting_user_delete', name='user_management_manage_single_vesting_user_delete'),
    url(r'^manage/vesting-users/(?P<user_id>[a-zA-Z0-9]+)/reactivate/?$', 'user_management.manage_single_vesting_user_reactivate', name='user_management_manage_single_vesting_user_reactivate'),
    url(r'^manage/vesting-users/(?P<user_id>[a-zA-Z0-9]+)/remove/?$', 'user_management.manage_single_vesting_user_remove', name='user_management_manage_single_vesting_user_remove'),
    url(r'^manage/users/(?P<user_id>[a-zA-Z0-9]+)/add-registrar/?$', 'user_management.user_add_registrar', name='user_management_user_add_registrar'),
    url(r'^manage/users/(?P<user_id>[a-zA-Z0-9]+)/add-vesting-org/?$', 'user_management.user_add_vesting_org', name='user_management_user_add_vesting_org'),
    url(r'^manage/vesting-users/add-user/?$', 'user_management.vesting_user_add_user', name='user_management_vesting_user_add_user'),
    url(r'^manage/account/leave-vesting-organization/?$', 'user_management.vesting_user_leave_vesting_org', name='user_management_vesting_user_leave_vesting_org'),
#    url(r'^manage/batch-convert/?$', 'user_management.batch_convert', name='user_management_batch_convert'),
#    url(r'^manage/export/?$', 'user_management.export', name='user_management_export'),
#    url(r'^manage/custom-domain/?$', 'user_management.custom_domain', name='user_management_custom_domain'),
#    url(r'^manage/users/?$', 'manage.users', name='manage_users'),
#    url(r'^manage/account/?$', 'manage.account', name='manage_account'),
#    url(r'^manage/activity/?$', 'manage.activity', name='manage_activity'),

    url(r'^cdx$', 'common.cdx', name='cdx'),

    # Our Perma ID catchall
    # url(r'^%s/?$' % r'(?P<guid>[^\./]+)', 'common.single_link_header', name='single_link_header'), # our pending, new, single link view
    url(r'^%s/?$' % r'(?P<guid>[^\./]+)', 'common.single_linky', name='single_linky'),

)

# debug-only serving of static and media assets
if settings.DEBUG:
    from django.contrib.staticfiles.views import serve as static_view
    from django.views.static import serve as media_view
    from mirroring.utils import may_be_mirrored
    urlpatterns += static(settings.STATIC_URL, may_be_mirrored(static_view)) + \
                   static(getattr(settings, 'DEBUG_MEDIA_URL', settings.MEDIA_URL), may_be_mirrored(media_view), document_root=settings.MEDIA_ROOT)

handler404 = 'perma.views.common.server_error_404'
handler500 = 'perma.views.common.server_error_500'
