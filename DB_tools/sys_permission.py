#!/usr/bin/env python
# encoding: utf-8


permission_datas = [
    # 获取个人用户信息
    {
        "name": "userinfo-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": "",
    },
    {
        "name": "userinfo-list",
        "method": ["GET", "POST"],
        "router_id": "",
    },
    # 用户管理权限
    {
        "name": "users-list",
        "method": ["GET", "POST"],
        "router_id": 2001,
    },
    {
        "name": "users-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 2001,
    },
    # 角色管理数据
    {
        "name": "roles-list",
        "method": ["GET", "POST"],
        "router_id": 2004,
    },
    {
        "name": "roles-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 2004,
    },
    # 权限管理数据
    {
        "name": "permissions-list",
        "method": ["GET", "POST"],
        "router_id": 2005,
    },
    {
        "name": "permissions-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 2005,
    },
    # 业务
    {
        "name": "articles-list",
        "method": ["GET", "POST"],
        "router_id": 3001,
    },
    {
        "name": "articles-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 3002,
    },
    {
        "name": "chapters-list",
        "method": ["GET", "POST"],
        "router_id": 3003,
    },
    {
        "name": "chapters-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 3003,
    },
    {
        "name": "features-list",
        "method": ["GET", "POST"],
        "router_id": 3003,
    },
    {
        "name": "features-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 3003,
    },
    {
        "name": "students-list",
        "method": ["GET", "POST"],
        "router_id": "",
    },
    {
        "name": "students-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": "",
    },
    {
        "name": "answers-list",
        "method": ["GET", "POST"],
        "router_id": "",
    },
    {
        "name": "answers-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": "",
    },
    {
        "name": "questions-list",
        "method": ["GET", "POST"],
        "router_id": "",
    },
    {
        "name": "questions-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": "",
    },
    {
        "name": "papers-list",
        "method": ["GET", "POST"],
        "router_id": "",
    },
    {
        "name": "papers-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": "",
    },
    {"name": "sms-list", "method": ["GET", "POST"], "router_id": ""},
    {
        "name": "sms-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": "",
    },
    {
        "name": "email-list",
        "method": ["GET", "POST"],
        "router_id": "",
    },
    {
        "name": "email-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": "",
    },
    # 路由管理
    {
        "name": "routers-list",
        "method": ["GET", "POST"],
        "router_id": "",
    },
    {
        "name": "routers-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": "",
    },
    # 用户组管理数据
    {
        "name": "group-list",
        "method": ["GET", "POST"],
        "router_id": "",
    },
    {
        "name": "group-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": "",
    },
    {
        "name": "api-root",
        "method": ["GET", "OPTIONS"],
        "router_id": "",
    },
    {
        "name": "docs-index",
        "method": ["GET", "OPTIONS"],
        "router_id": "",
    },
    {
        "name": "token_obtain_pair",
        "method": ["POST"],
        "router_id": "",
    },
    {
        "name": "token_refresh",
        "method": ["POST"],
        "router_id": "",
    },
    {
        "name": "token_verify",
        "method": ["POST"],
        "router_id": "",
    },
]
