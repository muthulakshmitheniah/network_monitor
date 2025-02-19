# decorators.py
from django.core.exceptions import PermissionDenied


def group_required(*group_names):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if (
                request.user.is_authenticated
                and request.user.groups.filter(name__in=group_names).exists()
            ):
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied

        return _wrapped_view

    return decorator
