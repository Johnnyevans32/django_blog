from django.views import generic
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Post, Comment

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(active=True)
        return context


# ── Session demo views (lecture material) ────────────────────────────────────

def cookie_session(request):
    """Step 1: sets a test cookie so the browser stores it."""
    request.session.set_test_cookie()
    return HttpResponse("<h1>Test cookie set! Now visit /deletecookie/ to check it.</h1>")


def cookie_delete(request):
    """Step 2: verifies the test cookie was accepted by the browser."""
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("<h1>Cookie created successfully – your browser accepts cookies!</h1>")
    else:
        response = HttpResponse("<h1>Your browser does NOT accept cookies.</h1>")
    return response


def create_session(request):
    """Stores 'name' and 'password' keys in the session."""
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>Session created! Values 'name' and 'password' are now stored.</h1>")


def access_session(request):
    """Reads session values; redirects to create/ if no session exists yet."""
    response = "<h1>Session Data</h1><br>"
    if request.session.get('name'):
        response += "Name: {0}<br>".format(request.session.get('name'))
        response += "Password: {0}<br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')


def delete_session(request):
    """Deletes the 'name' and 'password' keys from the session (data only)."""
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<h1>Session data cleared (session ID / cookie still active).</h1>")


def flush_session(request):
    """Completely destroys the session, including the session ID cookie."""
    request.session.flush()
    return HttpResponse("<h1>Session flushed – session ID and all data have been deleted.</h1>")
