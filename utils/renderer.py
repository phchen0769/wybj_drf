from rest_framework.renderers import JSONRenderer


# 自定义渲染器
class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code
        response = {
            "success": status_code < 400,
            "code": status_code,
            "data": data,
        }
        return super().render(response, accepted_media_type, renderer_context)
