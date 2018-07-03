from django.core.exceptions import PermissionDenied
from django.http import Http404

from rest_framework import exceptions
from rest_framework.response import Response
def custom_exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()
    code = 500   
    if isinstance(exc, exceptions.NotFound):
        code = -2
    elif isinstance(exc, (exceptions.PermissionDenied, exceptions.NotAuthenticated)):
        code = -1
    elif isinstance(exc, exceptions.ValidationError):
        code = 1  
        
    if isinstance(exc, (exceptions.APIException, exceptions.ValidationError)):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait
        if type(exc.detail) == dict:
            data = exc.detail
            data.update(code=code)
        else:
            data = {'code':code, 'detail': exc.detail}
        return Response(data, status=200, headers=headers)
    return None
