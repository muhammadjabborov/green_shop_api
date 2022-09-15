from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class CategoryPagination(PageNumberPagination):
    page_size = 4
    # page_size_query_param = 'page_size'
    max_page_size = 4


class JoinUserPagination(PageNumberPagination):
    page_size = 3
    # page_size_query_param = 'page_size'
    max_page_size = 3
