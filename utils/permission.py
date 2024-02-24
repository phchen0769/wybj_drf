from rest_framework.permissions import BasePermission
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions


# class MineAuthentication(BaseAuthentication):
#     """
#     自定义验证类
#     """

#     def authenticate(self, request):
#         # 读取用户请求token, 检验是否合法
#         token = request.query_params.get("token")
#         role = request.query_params.get("role")
#         if not token:
#             raise exceptions.AuthenticationFailed("认证失败")

#         print(request.user.name)
#         print(request.user.role)
#         print(request.auth)
#         return (
#             User("张三", role),
#             None,
#         )


class MinePermission(BasePermission):
    """
    自定义权限类
    """

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """

        METHOD_TYPE = {
            "GET": 1,
            "POST": 2,
            "DELETE": 3,
            "PUT": 4,
            "PATCH": 5,
            "OPTIONS": 6,
        }

        # 1、创建权限字典，以获取当前用户所有权限
        permission_dict = {}

        # 取出当前用户
        user = request.user

        # 获取用户的所有角色
        roles = user.role.all()

        # 对每个角色获取其所有的权限
        for role in roles:
            permissions = role.permission.all()

            for permission in permissions:
                # 创建空的方法列表
                method_list = []

                # 对每个权限获取其所有的方法，加入到方法列表中
                method_list.append(permission.method_type)

                # 把每个方法列表加入到权限字典中
                if permission_dict.get(permission.name):
                    permission_dict[permission.name].extend(method_list)
                    # 去重
                    permission_dict[permission.name] = list(
                        set(permission_dict[permission.name])
                    )
                else:
                    permission_dict[permission.name] = list(method_list)

        print(permission_dict)

        # 2.当前用户正在访问的URL和方式
        print(request.resolver_match.url_name, request.method)
        url_name = request.resolver_match.url_name
        method = METHOD_TYPE.get(request.method)

        # print(url_name, method)

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
