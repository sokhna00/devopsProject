from django.http import JsonResponse
from .models import CustomUser  # Import your User model

def user_list(request):
    # Query the database to get a list of users
    users = CustomUser.objects.all().values('username', 'email', 'first_name', 'last_name')
    
    # Convert the QuerySet to a list of dictionaries
    user_list = list(users)
    
    # Return the user list as JSON response
    return JsonResponse({'users': user_list})
