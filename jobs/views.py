from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Job
from .serializers import JobCardSerializer, JobDetailSerializer
from .utils import check_user_owner


class JobsViewSet(viewsets.ViewSet):
    def get_jobs_card(self, request):
        jobs = Job.objects.all()
        serializer = JobCardSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        if check_user_owner(request):
            serializer = JobDetailSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"message": "user token and owner of job does not match"},
                            status=status.HTTP_400_BAD_REQUEST)
