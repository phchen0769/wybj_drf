from rest_framework.renderers import JSONRenderer


# 自定义渲染器
class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code
        if status_code < 400:
            response = {
                "success": True,
                "code": status_code,
                "message": "请求成功。",
                "data": data,
            }
        else:
            response = {
                "success": False,
                "code": status_code,
                "message": data.get("detail"),
                "data": {},
            }
        return super().render(response, accepted_media_type, renderer_context)
