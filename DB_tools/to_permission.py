from permission_data import permission_data

# 把权限数据导入到数据库中
from apps.user.models import Permission, Role, UserProfile

# 1.创建权限
for permission in permission_data:
    # 1.1创建权限
    permission_obj = Permission.objects.create(
        name=permission["name"],
        method_type=permission["method_type"],
        menu_id=permission["menu_id"],
    )
