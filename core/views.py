from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from core import serializers, calculator


class FibonacciView(APIView):
    """fibonacci view in api/calculate/fibonacci"""

    @swagger_auto_schema(
        request_body=serializers.FibonacciSerializer,
        operation_description='calculate Fibonacci sequence ( 0 <= n <= 35 )',
        responses={
            status.HTTP_200_OK: 'you will get the response',
            status.HTTP_400_BAD_REQUEST: 'bad input or pass the limit'
        }
    )
    def post(self, request):
        ser = serializers.FibonacciSerializer(data=request.data)

        if ser.is_valid():
            inputs = ser.validated_data.get('n', None)
            result = calculator.fibonacci(n=inputs)
            response = {
                'success': True,
                'status': status.HTTP_200_OK,
                'input': inputs,
                'result': result,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class FactorialView(APIView):
    """factorial view in api/calculate/factorial"""

    inputs_param = openapi.Parameter(
        'n', openapi.IN_BODY,
        'Factorial input', required=True, type=openapi.TYPE_INTEGER
    )

    @swagger_auto_schema(
        request_body=serializers.FactorialSerializer,
        operation_description='calculate Factorial of Integer value ( 0 <= n <= 170 )',
        responses={
            status.HTTP_200_OK: 'you will get the response',
            status.HTTP_400_BAD_REQUEST: 'bad input or pass the limit'
        }
    )
    def post(self, request):
        ser = serializers.FactorialSerializer(data=request.data)

        if ser.is_valid():
            inputs = ser.validated_data.get('n', None)
            result = calculator.factorial(n=inputs)
            response = {
                'success': True,
                'status': status.HTTP_200_OK,
                'input': inputs,
                'result': result,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class AckermannView(APIView):
    """ackermann view in api/calculate/factorial"""

    @swagger_auto_schema(
        request_body=serializers.AckermannSerializer,
        operation_description='calculate Ackermann for provided m and n values '
                              '( 0 <= n <= 230 , 0 <= m <= 4 ) ',
        responses={
            status.HTTP_200_OK: 'you will get the response',
            status.HTTP_400_BAD_REQUEST: 'bad input or pass the limit'
        }
    )
    def post(self, request):
        ser = serializers.AckermannSerializer(data=request.data)

        if ser.is_valid():
            m = ser.validated_data.get('m', None)
            n = ser.validated_data.get('n', None)
            result = calculator.ackermann(**ser.validated_data)
            response = {
                'success': True,
                'status': status.HTTP_200_OK,
                'm': m,
                'n': n,
                'result': result,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)