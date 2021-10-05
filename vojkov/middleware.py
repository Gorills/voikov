from django.utils.deprecation import MiddlewareMixin
from .models import Page




class GetPage(MiddlewareMixin):
    def process_request(self, request):

        page_list= Page.objects.all()
       
        request.page_list = page_list
        
        print(request.page_list)
        return None