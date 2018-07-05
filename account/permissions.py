from rest_framework.authentication import  BaseAuthentication
class MyBasicAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user = getattr(request._request, 'user', None)
        # Unauthenticated, CSRF validation not required
        if not user or not user.is_active:
            return None
            # CSRF passed with authenticated user
        return (user, None)
