from rest_framework import serializers


class FibonacciSerializer(serializers.Serializer):
    n = serializers.IntegerField(required=True)

    def validate_n(self, value):
        if value > 35:
            raise serializers.ValidationError(
                'you should provide number less than 35',
                code='pass_limit'
            )
        if value < 0:
            raise serializers.ValidationError(
                'you should enter non-negative numbers.',
                code='neg_number'
            )

        return value


class FactorialSerializer(serializers.Serializer):
    n = serializers.IntegerField(required=True)

    def validate_n(self, value):
        if value > 170:
            raise serializers.ValidationError(
                'you should provide number less than 170',
                code='pass_limit'
            )
        if value < 0:
            raise serializers.ValidationError(
                'you should enter non-negative numbers.',
                code='neg_number'
            )

        return value