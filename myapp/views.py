from django.shortcuts import render, get_object_or_404

from myapp.models import User


def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'myapp/index.html', {'user': user})
