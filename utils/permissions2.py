from rest_framework.permissions import BasePermission
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

class MineAuthentication(BaseAuthentication):
    """
    自定义验证类
    """
    def authenticate(self,request):
        # 读取用户请求token, 检验是否合法
        token = request.query_params.get("token")
        role = request.query_params.get("role")
        if not token:
            raise exceptions.AuthenticationFailed("认证失败")
        
        print(request.user.name)
        print(request.user.role)
        print(request.auth)
        return(User("张三",role),None,)


class MinePermission(BasePermission):
    """
    自定义权限类
    """
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        print("判断权限", request.user.role)

        # 1.当前用户所有的权限
        # from django.conf import settings
        from wybj_drf import settings
        permission_dict = settings.PERMISSIONS[request.user.role]

        # 2.当前用户正在访问的URL和方式
        print(request.resolver_match.url_name, request.method)
        url_name = request.resolver_match.url_name
        method = request.method

        # 3.权限判断
        method_list = permission_dict.get(url_name)
        if not method_list:
            return False
        if method in method_list:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True