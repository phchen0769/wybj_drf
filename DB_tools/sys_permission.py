#!/usr/bin/env python
# encoding: utf-8


permission_datas = [
    {
        "name": "users-list",
        "method": ["GET", "POST"],
        "router_id": 2003,
    },
    {
        "name": "users-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 2003,
    },
    {
        "name": "userinfo-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 2001,
    },
    {
        "name": "userinfo-list",
        "method": ["GET", "POST"],
        "router_id": 2002,
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
        "router_id": 1001,
    },
    {
        "name": "students-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 1001,
    },
    {
        "name": "answers-list",
        "method": ["GET", "POST"],
        "router_id": 1001,
    },
    {
        "name": "answers-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 1001,
    },
    {
        "name": "questions-list",
        "method": ["GET", "POST"],
        "router_id": 1001,
    },
    {
        "name": "questions-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 1001,
    },
    {
        "name": "papers-list",
        "method": ["GET", "POST"],
        "router_id": 1001,
    },
    {
        "name": "papers-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 1001,
    },
    {"name": "sms-list", "method": ["GET", "POST"], "router_id": 1001},
    {
        "name": "sms-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 1001,
    },
    {
        "name": "email-list",
        "method": ["GET", "POST"],
        "router_id": 1001,
    },
    {
        "name": "email-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 1001,
    },
    # 路由管理
    {
        "name": "routers-list",
        "method": ["GET", "POST"],
        "router_id": 1001,
    },
    {
        "name": "routers-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 1001,
    },
    # 用户组管理数据
    {
        "name": "group-list",
        "method": ["GET", "POST"],
        "router_id": 1001,
    },
    {
        "name": "group-detail",
        "method": ["GET", "DELETE", "PUT", "PATCH", "OPTIONS"],
        "router_id": 1001,
    },
    {
        "name": "api-root",
        "method": ["GET", "OPTIONS"],
        "router_id": 1001,
    },
    {
        "name": "docs-index",
        "method": ["GET", "OPTIONS"],
        "router_id": 1001,
    },
    {
        "name": "token_obtain_pair",
        "method": ["POST"],
        "router_id": 1001,
    },
    {
        "name": "token_refresh",
        "method": ["POST"],
        "router_id": 1001,
    },
    {
        "name": "token_verify",
        "method": ["POST"],
        "router_id": 1001,
    },
]
