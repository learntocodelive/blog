from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.versioning import NamespaceVersioning
from functools import wraps
from rest_framework.response import Response


def validate_api(*main_args, **main_kwargs):
    def decorator_func(func, *args, **kwargs):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as error:
                print("Error in api call: ", error)
                return BaseViewSet.error_response(
                    msg=f"Error in api call. Msg- {error}"
                )

        return func_wrapper

    return decorator_func


class BaseViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    # versioning_class = NamespaceVersioning

    @staticmethod
    def error_response(msg=None, form_errors=None, status_code=500):
        return Response(
            {
                "ok": False,
                "data": None,
                "errors": {"msg": msg, "form_errors": form_errors},
            },
            status=status_code,
        )

    @staticmethod
    def success_response(data=None, status_code=200):
        return Response({"ok": True, "data": data}, status=status_code)