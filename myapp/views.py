from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    response = requests.get("https://api.github.com/users/naveenkrnl")
    print(response.status_code)
    data =response.text
    parsed_data = json.loads(data)
    print(parsed_data)
    """login = parsed_data['login']
    id = parsed_data['id']
    followers = parsed_data["followers"]
    info = {
        "login":login,
        "id":id,
        "followers":followers
    }"""
    return render(request,'myapp/home.html',parsed_data)