from rest_framework.views import APIView

from pipeline.models import CompanyInfo
from pipeline.serializer import WhiteListSerializer,CreditSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class WhiteListInfo(APIView):

    def get_object(self, email):
        try:
            return CompanyInfo.objects.get(email=email)
        except CompanyInfo.DoesNotExist:
            raise Http404

    def get(self, request):
        print('para',request.query_params)
        if(request.query_params != None and request.query_params['email'] != None):
            k = request.query_params['email']

        companyInfos = self.get_object(k)
        serializer = WhiteListSerializer(companyInfos)
        return Response(serializer.data)

    def post(self, request):
        serializer = WhiteListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        if (request.query_params != None and request.query_params['email'] != None):
            k = request.query_params['email']

        companyInfos = self.get_object(k)
        serializer = WhiteListSerializer(companyInfos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreditInfo(APIView):

    def get_object(self, email):
        try:
            return CompanyInfo.objects.get(email=email)
        except CompanyInfo.DoesNotExist:
            raise Http404

    def get(self, request):
        print('para', request.query_params)
        if (request.query_params != None and request.query_params['email'] != None):
            k = request.query_params['email']

        companyInfos = self.get_object(k)
        serializer = CreditSerializer(companyInfos)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = CreditSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        if (request.query_params != None and request.query_params['email'] != None):
            k = request.query_params['email']

        companyInfos = self.get_object(k)
        serializer = CreditSerializer(companyInfos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
