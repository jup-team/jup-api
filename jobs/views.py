from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Job
from .serializers import JobCardSerializer, JobDetailSerializer


class JobsViewSet(viewsets.ViewSet):
    def get_jobs_card(self, request):
        jobs = Job.objects.all()
        serializer = JobCardSerializer(jobs, many=True)
        return Response(serializer.data)
