from django.urls import path , re_path , include



from . import views

#app_name = "backend.fighter"
urlpatterns = [
    #path('fighters/', views.IndexView.as_view(), name='index'),
    #path('fighters/<int:id>', views.fighter_list, name='fighter_list'),
    #re_path(r'^(?P<id>[\w-]+)/?$', views.fighter_detail, name='fighter_detail'),
    #re_path(r'^$', Index_view.as_view()),
    #re_path(r'^archive/$', archive_view.as_view()),
    path('', views.fighter_list, name='fighter_list'),
    path('detail/<int:id>/', views.fighter_detail, name='fighter_detail'),
    #path('', views.fighter_list, name='fighter_list_plugin'),
    #re_path('detail_selected/<int:id>/', views.fighter_detail, name='detail_selected'),


    #path('get_fighter/', views.get_fighter, name='get_fighter'),
    #path('get_fighter/<int:id>', views.get_fighter, name='get_fighter'),
    #re_path(r'^$', views.get_fighters, name='get_fighters'),
    #re_path(r'^get_fighter/$', views.get_fighter, name='get_fighter'), 
]
    #re_path(r'^fighter_detail/<int:id>/', archive_view.as_view()),
    
    #path(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #path(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #path(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),


