import webbrowser
from pprint import pprint as pp

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Url


class RestoreUrlsAPIView(APIView):
    def get(self, *args, **kwargs):
        urls = []
        for url_tuple in list(Url.objects.all().values_list('url')):
            urls.append(url_tuple[0])
        # pp(urls)
        return Response({'urls': urls}, status=status.HTTP_200_OK)


class BatchTabsAPIView(APIView):
    def post(self, *args, **kwargs):
        urls = self.request.data['urls']
        Url.objects.all().delete()
        for url in urls:
            # print(url)
            Url.objects.create(url=url)
            webbrowser.open_new_tab(url)

        return Response({'msg': 'BatchTabs命令接收成功'}, status=status.HTTP_200_OK)
