import subprocess

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CollectstaticAPIView(APIView):
    def post(self, *args, **kwargs):
        # subprocess此模块用于代替一些老旧的模块与功能，例如：os.system, os.spawn*
        subprocess.run(['python', 'manage.py', 'collectstatic'])
        return Response({'msg': 'Collectstatic命令接收成功'}, status=status.HTTP_200_OK)


class MigrateAPIView(APIView):
    def post(self, *args, **kwargs):
        subprocess.run(['python', 'manage.py', 'makemigrations'])
        subprocess.run(['python', 'manage.py', 'migrate'])
        return Response({'msg': 'Migrate命令接收成功'}, status=status.HTTP_200_OK)
