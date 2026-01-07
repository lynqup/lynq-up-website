# studybud/middleware.py
from django.http import HttpResponsePermanentRedirect

class RedirectApexToWWW:
    """
    Redirect lynqup.net → www.lynqup.net
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host == "lynqup.net":
            new_url = request.build_absolute_uri().replace("lynqup.net", "www.lynqup.net", 1)
            return HttpResponsePermanentRedirect(new_url)
        return self.get_response(request)
