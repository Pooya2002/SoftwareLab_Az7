from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CustomUser
from .forms import UserCreateForm


@csrf_exempt
def login_func(request):
    if request.method != 'POST':
        return JsonResponse({'error': "POST method required"})

    import json
    try:
        data = json.loads(request.body)  
        username = data.get('username')
        password = data.get('password')
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON', 'details': str(e)}, status=400)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'message': 'Login successful'})
    else:
        return JsonResponse({'error': 'Invalid username or password', 'detail': password}, status=400)

def user_list(request):
    if not request.user.is_authenticated:
        return JsonResponse({'message': "User is not logged in"})

    users = CustomUser.objects.all()
    data = [{'id': user.id, 'username': user.username} for user in users]
    return JsonResponse(data, safe=False)


def user_me(request):
    if not request.user.is_authenticated:
        return JsonResponse({'message': "User is not logged in"})

    user = request.user
    data = {'id': user.id, 'username': user.username}
    return JsonResponse(data)

@csrf_exempt
def user_create(request):
    if request.method != 'POST':
        return JsonResponse({'error': "POST method required"})

    try:
        data = json.loads(request.body)
        print(data)  
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON', 'details': str(e)}, status=400)

    form = UserCreateForm(data)
    if form.is_valid():
        user = form.save()
        data = {'id': user.id, 'username': user.username}
        return JsonResponse(data)
    else:
        print(form.errors)  
        return JsonResponse({'error': 'Invalid data', 'details': form.errors}, status=400)

@csrf_exempt
def user_delete(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({'message': "User is not logged in"})

    user = get_object_or_404(CustomUser, pk=pk)
    user.delete()
    return JsonResponse({'message': 'User deleted successfully'})

