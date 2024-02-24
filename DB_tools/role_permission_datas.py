from permission_datas import permission_datas

# 计算出所有权限的数量
all_permission = 0
for permission_data in permission_datas:
    all_permission += permission_data["method_type"].__len__()

role_permission_datas = [
    {
        "role_id": 1,
        "permission_id": list(range(1, all_permission + 1)),
    },
    {
        "role_id": 2,
        "permission_id": list(range(1, 34)),
    },
    {
        "role_id": 3,
        "permission_id": list(range(1, 12)),
    },
]
