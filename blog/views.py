import os

from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from .serializers import UploadSerializer
from .main import filter_text

# Create your views here.

class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response({"message": "Send only txt files"})

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')

        if not file_uploaded:
            return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            filename = fs.save(file_uploaded.name, file_uploaded)
            response = {"message": "Successfully posted"}
            filter_text(filename)
        except Exception as e:
            response = {"error": str(e)}
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(response, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_items(request):
    name = "filter.txt"
    image_path = os.path.join(settings.MEDIA_ROOT,name)

    if not os.path.exists(image_path):
        raise Http404("Text does not exist")

    with open(image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="text/plain")  # Adjust the content type as needed
        response['Content-Disposition'] = f'attachment; filename="{name}"'
        return response