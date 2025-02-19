from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def group_required(*group_names):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('/admin/login/')  # Redirect to login

            if request.user.groups.filter(name__in=group_names).exists():
                return view_func(request, *args, **kwargs)

            raise PermissionDenied  # Only raise if user is authenticated but lacks permission

        return _wrapped_view

    return decorator
