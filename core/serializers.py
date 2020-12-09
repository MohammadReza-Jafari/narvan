from rest_framework import serializers


class FibonacciSerializer(serializers.Serializer):
    """serializer for fibonacci function"""
    n = serializers.IntegerField(required=True)

    def validate_n(self, value):
        """validating n"""
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
    """serializer for factorial function"""
    n = serializers.IntegerField(required=True)

    def validate_n(self, value):
        """validating n"""
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


class AckermannSerializer(serializers.Serializer):
    """serializer for ackermann function"""
    m = serializers.IntegerField(required=True)
    n = serializers.IntegerField(required=True)

    def validate_m(self, value):
        """validating m"""
        if value > 4:
            raise serializers.ValidationError(
                'you should provide value for m less than 4',
                code='pass_limit'
            )
        if value < 0:
            raise serializers.ValidationError(
                'you should enter non-negative numbers.',
                code='neg_number'
            )

        return value

    def validate_n(self, value):
        """validating n"""
        if value > 100000:
            raise serializers.ValidationError(
                'you should provide value for n less than 100000',
                code='pass_limit'
            )
        if value < 0:
            raise serializers.ValidationError(
                'you should enter non-negative numbers.',
                code='neg_number'
            )

        return value

    def validate(self, attrs):
        """validating m,n together"""
        m = attrs.get('m', None)
        n = attrs.get('n', None)

        if m == 3 and n > 60:
            raise serializers.ValidationError(
                'With m=3 you could choose value for n between 0 and 60',
                'limitation'
            )

        if m == 4 and n > 1:
            raise serializers.ValidationError(
                'With m=4 you could choose 0,1 for n',
                'limitation'
            )

        return attrs
