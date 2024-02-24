import os
import django

# 设置django环境，否则无法使用django的ORM
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()


# 导入菜单数据
from DB_tools.menu_datas import menu_datas

# 导入权限数据
from DB_tools.permission_datas import permission_datas

# 导入角色数据
from DB_tools.role_datas import role_datas

# 导入角色权限数据
from DB_tools.role_permission_datas import role_permission_datas

# 把权限数据导入到数据库中
from apps.user.models import Menu, Permission, Role


# 导入菜单数据
def import_menu():
    for menu in menu_datas:
        Menu.objects.create(
            name=menu["name"],
            icon=menu["icon"],
            path=menu["path"],
            # 如果sub_menu有值，就取出对应的菜单对象，否则就是None
            sub_menu=(
                Menu.objects.get(id=menu["sub_menu"]) if menu["sub_menu"] else None
            ),
        )


# 导入权限数据
def import_permission():
    # 1.遍历权限名称
    for permission in permission_datas:
        # 遍历方法名
        for method in permission["method_type"]:
            Permission.objects.create(
                method_type=method,
                name=permission["name"],
                menu_id=permission["menu_id"],
            )


# 导入角色数据
def import_role():
    for role in role_datas:
        Role.objects.create(
            role_type=role["role_type"],
        )


# 导入角色权限数据
def import_role_permission():
    for role_permission_data in role_permission_datas:
        role = Role.objects.get(id=role_permission_data["role_id"])
        for permission in role_permission_data["permission_id"]:
            permission = Permission.objects.filter(
                id__in=role_permission_data["permission_id"]
            )
            role.permission.set(permission)


if __name__ == "__main__":
    import_menu()
    import_permission()
    import_role()
    import_role_permission()
    print("导入成功")
