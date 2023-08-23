from django.shortcuts import render
from api.models import profile
from api.serializers import profileSerializers
from rest_framework.views import APIView
from rest_framework.response import Response

class profileView(APIView):
    def get(self, request, format=None):
        candidates = profile.objects.all()
        serializer = profileSerializers(candidates, many=True)

        return Response({'msg':'Data Fetched Successfully',
                         'data':serializer.data})
    
    def post(self, request, format=None):
        serializer = profileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'msg':'Data Saved Successfully',
                             'data':serializer.data})
        
        return Response({'msg':'Something Wrong !',
                             'data':serializer.error})
        

