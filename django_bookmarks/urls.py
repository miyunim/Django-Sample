import os.path
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from bookmarks.views import *
from bookmarks.feeds import *

site_media = os.path.join(os.path.dirname(__file__), 'site_media')

feeds = {
  'recent': RecentBookmarks,
  'user': UserBookmarks
}

urlpatterns = patterns('',
	# Browsing
	(r'^$', main_page),
	(r'^popular/$', popular_page),
	(r'^user/(\w+)/$', user_page),
  (r'^tag/([^\s]+)/$', tag_page),
  (r'^tag/$', tag_cloud_page),
  (r'^search/$', search_page),
  (r'^bookmark/(\d+)/$', bookmark_page),
  
  # Comments
  (r'^comments/', include('django.contrib.comments.urls.comments')),

	# Ajax
  (r'^ajax/tag/autocomplete/$', ajax_tag_autocomplete),

  # Session management
	(r'^login/$', 'django.contrib.auth.views.login'),
	(r'^logout/$', logout_page),
	(r'^register/$', register_page),
	(r'^register/success/$', direct_to_template,
		{ 'template': 'registration/register_success.html' }),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
		{ 'document_root': site_media }),

	# Account management
	(r'^save/$', bookmark_save_page),
  (r'^vote/$', bookmark_vote_page),
  
  # Admin interface
  (r'^admin/', include('django.contrib.admin.urls')),

  # Feeds
  (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

)



