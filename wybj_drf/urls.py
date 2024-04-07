"""
URL configuration for wybj_drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

# 从DRF中引入路由组件, 此组件的作用是用来替代Django原生路由
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter, SimpleRouter

# 导入自定义token认证模块
from utils.mytoken import MyTokenObtainPairView

# 导入simplejwt认证模块
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# 从user app中导入viewset
from apps.user.views import (
    UserViewSet,
    SmsCodeViewSet,
    EmailCodeViewSet,
    PermissionViewSet,
    RoleViewSet,
    CurrentUserViewSet,
    RouterViewSet,
)

# 从score app中导入viewset
from apps.score.views import (
    StudentViewSet,
    AnswerViewSet,
    QuestionViewSet,
    PaperViewSet,
)

# 从article app中导入ArticleViewSet
from apps.article.views import ArticleViewSet, ChapterViewSet

# 从feature app中导入viewset
from apps.feature.views import FeatureViewSet


# simple router 不会自动添加末尾的斜杠
router = SimpleRouter(trailing_slash=False)

# user app的url配置
router.register("sms", SmsCodeViewSet, basename="sms")
router.register("email", EmailCodeViewSet, basename="email")
router.register("permissions", PermissionViewSet, basename="permissions")
router.register("roles", RoleViewSet, basename="roles")
router.register("routers", RouterViewSet, basename="routers")
router.register("userinfo", CurrentUserViewSet, basename="userinfo")
router.register("users", UserViewSet, basename="users")
# router.register("user-role", UserViewSet, basename="user-role")
# router.register("register", CurrentUserViewSet, basename="register")

# score app的url配置
router.register("students", StudentViewSet, basename="students")
router.register("answers", AnswerViewSet, basename="answers")
router.register("questions", QuestionViewSet, basename="questions")
router.register("papers", PaperViewSet, basename="papers")

# article app的url配置
router.register("articles", ArticleViewSet, basename="articles")
router.register("chapters", ChapterViewSet, basename="chapters")

# featurn app的url配置
router.register("features", FeatureViewSet, basename="features")


urlpatterns = [
    # api文档功能
    path("docs", include_docs_urls(title="五育并举系统")),
    # api页面的登录功能
    path("api-auth", include("rest_framework.urls")),
    # api页面的根路径
    path("api/", include(router.urls)),
    # simplejwt 验证用户名密码，并产生token
    path("api/login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # simplejwt 刷新token
    path("refresh", TokenRefreshView.as_view(), name="token_refresh"),
    # simplejwt 验证token
    path("verify", TokenVerifyView.as_view(), name="token_verify"),
]
