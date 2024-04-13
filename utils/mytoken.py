from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response


class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        custom_response = {
            "token": response.data["access"],
            "refresh_token": response.data["refresh"],
        }
        return Response(custom_response)
