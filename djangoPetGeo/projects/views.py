from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Projects, GeoPoint, GeoLine, GeoPoly
from .serializers import ProjectListSerializer, ProjectSerializer, GeoPointSerializer, GeoLineSerializer, GeoPolySerializer


class ProjectListView(APIView):
    def get(self, request):
        projects = Projects.objects.all()
        serializer = ProjectListSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        project = ProjectSerializer(data=request.data)
        if project.is_valid():
            project.save()
        return Response(status=203)


class ProjectView(APIView):
    def get(self, request, pk):
        project = Projects.objects.get(id=pk)
        geoPointQuery = GeoPoint.objects.filter(project=pk)
        geoLineQuery = GeoLine.objects.filter(project=pk)
        geoPolyQuery = GeoPoly.objects.filter(project=pk)
        geoPointSerializer = GeoPointSerializer(geoPointQuery, many=True)
        geoLineSerializer = GeoLineSerializer(geoLineQuery, many=True)
        geoPolySerializer = GeoPolySerializer(geoPolyQuery, many=True)
        geoSerializerDict = {'geo_data':[]}
        geoSerializerDict['geo_data'].append(geoPointSerializer.data)
        geoSerializerDict['geo_data'].append(geoLineSerializer.data)
        geoSerializerDict['geo_data'].append(geoPolySerializer.data)
        serializer = ProjectSerializer(project)
        result = list()
        result.append(serializer.data)
        result.append(geoSerializerDict)
        return Response(result)


class GeoPointView(APIView):
    def get(self, request):
        geoPointQuery = GeoPoint.objects.all()
        geoPointSerializer = GeoPointSerializer(geoPointQuery, many=True)
        return Response(geoPointSerializer.data)