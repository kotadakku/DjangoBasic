from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
from django.views import View

from .models import Courses
from .serializers import GetAllCourseSerializer, CourceSerializer


class CoursesView(View):
    template_name = "courses/courses_detail.html"
    def get(self, request, id, *args, **kwargs):
        context ={}
        if id is not None:
            obj = get_object_or_404(Courses, id =id)
            context['object']= obj
        return render(request, self.template_name, context)

class CoursesListView(View):
    template_name = "courses/courses_list.html"
    queryset = Courses.objects.all()
    def get_queryset(self):
        return self.queryset
    def get(self, request):
        return render(request, self.template_name,{'object_list':self.queryset})
    
# class MyListView(CoursesListView):
#     queryset = Courses.objects.filter(id=1)


class GetAllCource(APIView):
    queryset = Courses.objects.all()
    def get(self, request):
        list_course = Courses.objects.all()
        mydata = GetAllCourseSerializer(list_course, many=True)
        return Response(data=mydata.data, status= status.HTTP_200_OK)
    def post(self, request):
        mydata = CourceSerializer(data=request.data)
        if mydata.is_valid():
            title = mydata.data['title']
            content = mydata.data['content']
            price = mydata.data['price']
            cs = Courses.objects.create(title =title , content =content , price =price)
            return Response("ok", status= status.HTTP_200_OK)
        else:
            return Response("Du lieu sai", status=status.HTTP_400_BAD_REQUEST)


