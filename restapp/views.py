import json

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .serializer import *
from .models import ToDo, TimingTodo
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@api_view(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        return Response({
            'Status': 200,
            'Message': 'Django Rest_framework all Set to go ahead!',
            'Method': f'You canlled {request.method} method'
        })

    elif request.method == "POST":
        return Response({
            'Status': 200,
            'Message': 'Django Rest_framework all Set to go ahead!',
            'Method': f'You canlled {request.method} method'
        })


@api_view(['GET'])
def get_Todo(request):
    todo_objs = ToDo.objects.all()
    serializer = TodoSerializer(todo_objs, many=True)

    return Response({
        'Status': True,
        'Message': 'Todo Fatched',
        'data': serializer.data
    })


@api_view(['POST'])
def post_Todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data=data)

        if serializer.is_valid():
            print(data)

            serializer.save()
            return Response({
                'Status': True,
                'Message': 'Success data',
                'data': serializer.data
            })
        else:
            return Response({
                'Status': False,
                'Message': 'Invalid data',
                'data': serializer.errors
            })
    except Exception as E:
        print(E)

        return Response({
            'Status': True,
            'Message': 'Something Went Wrong !!',

        })


@api_view(['PATCH'])
def patch_Todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'Status': 302,
                'Message': 'must needed uid',
                'data': dict()

            })

        obj = ToDo.objects.get(uid=data['uid'])
        serializer = TodoSerializer(obj, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'Status': True,
                'Message': 'Success data',
                'data': serializer.data
            })
        else:
            return Response({
                'Status': False,
                'Message': 'Invalid data',
                'data': serializer.errors
            })

    except Exception as E:
        print(E)
        return Response({
            'Status': False,
            'Message': 'invalid uid',

        })


class TodoView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        print(request.user)
        todo_objs = ToDo.objects.all()
        serializer = TodoSerializer(todo_objs, many=True)

        return Response({
            'Status': True,
            'Message': 'Todo Fatched',
            'data': serializer.data
        })

    def post(self, request):
        try:
            data = request.data
            serializer = TodoSerializer(data=data)

            if serializer.is_valid():
                print(data)

                serializer.save()
                return Response({
                    'Status': True,
                    'Message': 'Success data',
                    'data': serializer.data
                })
            else:
                return Response({
                    'Status': False,
                    'Message': 'Invalid data',
                    'data': serializer.errors
                })
        except Exception as E:
            print(E)

            return Response({
                'Status': True,
                'Message': 'Something Went Wrong !!',

            })

    def patch(self, request):
        try:
            data = request.data
            if not data.get('uid'):
                return Response({
                    'Status': 302,
                    'Message': 'must needed uid',
                    'data': dict()

                })

            obj = ToDo.objects.get(uid=data['uid'])
            serializer = TodoSerializer(obj, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'Status': True,
                    'Message': 'Success data',
                    'data': serializer.data
                })
            else:
                return Response({
                    'Status': False,
                    'Message': 'Invalid data',
                    'data': serializer.errors
                })

        except Exception as E:
            print(E)
            return Response({
                'Status': False,
                'Message': 'invalid uid',

            })


class TodoViewSet(viewsets.ModelViewSet):

    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['GET'])
    def get_timing_todo(self, request):
        objs = TimingTodo.objects.all()
        serializers = TodoTimingSerializer(objs, many=True)

        return Response({
            'status': True,
            'message': 'timing todo fatched',
            'data': serializers.data
        })

    @action(detail=False, methods=['post'])
    def add_date_to_todo(self, request):

        try:
            data = request.data
            serializer = TodoTimingSerializer(data=data)
            print(data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'Status': True,
                    'Message': 'Success data',
                    'data': serializer.data
                })

            print(serializer.errors)

            return Response({
                'Status': False,
                'Message': 'invalid data',
                'data': serializer.errors
            })

        except Exception as E:

            return Response({
                'Status': False,
                'Message': 'Something went Wrong',
                'data': E

            })
