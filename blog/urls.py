from . import views
from django.urls import path

urlpatterns = [
    # ── Blog views ──────────────────────────────────────────────────────────
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

    # ── Session demo URLs (lecture material) ─────────────────────────────────
    # Cookie check
    path('testcookie/', views.cookie_session, name='testcookie'),
    path('deletecookie/', views.cookie_delete, name='deletecookie'),
    # Create / access / delete session data
    path('create/', views.create_session, name='create_session'),
    path('access/', views.access_session, name='access_session'),
    path('delete/', views.delete_session, name='delete_session'),
    # Fully flush (destroy) the session
    path('flush/', views.flush_session, name='flush_session'),
]
