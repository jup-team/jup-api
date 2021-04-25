def check_user_owner(request):
    return request.user.id == request.data.get('owner')
