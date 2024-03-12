from rest_framework.views import exception_handler  # 继承默认exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)  # 重新定义

    if response is not None:
        response.data.clear()
        # response.data["success"] = response.status_code < 400
        # response.data["code"] = response.status_code
        # response.data["data"] = []

        if response.status_code == 404:
            try:
                response.data["message"] = response.data.pop("detail")
                # response.data["message"] = "未找到"
            except KeyError:
                response.data["message"] = "未找到"

        if response.status_code == 400:
            response.data["message"] = "输入错误"

        elif response.status_code == 401:
            response.data["message"] = "未认证"

        elif response.status_code >= 500:
            response.data["message"] = "服务器错误"

        elif response.status_code == 403:
            response.data["message"] = "权限不允许"

        elif response.status_code == 405:
            response.data["message"] = "请求不允许"
        else:
            response.data["message"] = "未知错误"
    return response
