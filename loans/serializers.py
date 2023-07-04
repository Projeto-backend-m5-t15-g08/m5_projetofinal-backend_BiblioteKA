from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken
from copies.models import Copy
from loans.models import Loan


class LoanSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    return_date = serializers.DateTimeField(read_only=True)
    copy_id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data: dict):
        token = self.context["request"].auth.token
        decoded_token = AccessToken(token)
        user_id = decoded_token["user_id"]
        copy_id = self.context["view"].kwargs["copy_id"]

        copy = Copy.objects.get(id=copy_id)

        copy.active_loan = True
        copy.save()

        return Loan.objects.create(**validated_data, user_id=user_id, copy_id=copy_id)