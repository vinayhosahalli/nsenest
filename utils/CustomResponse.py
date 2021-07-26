from rest_framework.response import Response
from rest_framework import status


def success(data=None, message='Success'):
    return Response({'message': message, 'data': data}, status=status.HTTP_200_OK)


def notfound(data=None, message='Not Found'):
    return Response({'message': message, 'data': data}, status=status.HTTP_404_NOT_FOUND)





