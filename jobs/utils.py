def check_user_owner(request):
    print({request.user.id}, {request.data.get('owner')})
    return request.user.id == request.data.get('owner')
