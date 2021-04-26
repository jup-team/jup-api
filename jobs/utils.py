def check_user_owner(request):
    print(request.data.get('owner'), request.user.id)
    return request.user.id == request.data.get('owner')
