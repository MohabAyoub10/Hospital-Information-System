def permission_exception_handler(request, role):
    try:
            return bool(request.user.role == role)
    except:
            return False
