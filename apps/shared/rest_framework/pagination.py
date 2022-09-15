from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    pass


class CategoryPagination(PageNumberPagination):
    page_size = 4
    # page_size_query_param = 'page_size'
    max_page_size = 4


class JoinUserPagination(PageNumberPagination):
    page_size = 3
    # page_size_query_param = 'page_size'
    max_page_size = 3
