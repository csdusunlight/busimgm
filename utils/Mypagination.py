from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework.response import Response
class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pageSize'
    def get_paginated_response(self, data):
        if self.page.paginator.count>0:
            code = 1
        else:
            code = 0
        return Response(OrderedDict([
            ('code', code),
            ('recordCount', self.page.paginator.count),
            ('pageCount', self.page.paginator.num_pages),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))