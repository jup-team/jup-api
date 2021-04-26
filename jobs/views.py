from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from .models import Job, Position
from .serializers import JobCardSerializer, JobDetailSerializer, PositionSerializer


class PositionViewSet(mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class JobsViewSet(viewsets.ViewSet):
    def get_jobs_card(self, request):
        jobs = Job.objects.all()
        serializer = JobCardSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobDetailSerializer(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
