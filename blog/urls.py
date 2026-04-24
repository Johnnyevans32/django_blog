from . import views
from django.urls import path

urlpatterns = [
    # ── Blog views ──────────────────────────────────────────────────────────
    path('', views.PostList.as_view(), name='home'),

    # Cookie check
    path('testcookie/', views.cookie_session, name='testcookie'),
    path('deletecookie/', views.cookie_delete, name='deletecookie'),
    # Create / access / delete session data
    path('create/', views.create_session, name='create_session'),
    path('access/', views.access_session, name='access_session'),
    path('delete/', views.delete_session, name='delete_session'),
    # Fully flush (destroy) the session
    path('flush/', views.flush_session, name='flush_session'),

    path('redirect/', views.example_for_redirect, name='example_redirect'),
    path('djangotutor/', views.TutorialRedirect.as_view(), name='djangotutor'),

    path('cookies/set/', views.cookie_set_demo, name='cookie_set_demo'),
    path('cookies/get/', views.cookie_get_demo, name='cookie_get_demo'),
    path('cookies/delete/', views.cookie_remove_demo, name='cookie_remove_demo'),

    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
