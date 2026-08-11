
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data.get("userName")
    password = data.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})
    else:
        return JsonResponse({"userName": username, "status": "Failed"})

from django.contrib.auth import logout

def logout_request(request):
    logout(request)
    username = request.user.username if request.user.is_authenticated else ""
    return JsonResponse({"userName": username, "status": "Logged out"})

# Data mẫu cho dealers và reviews (thường lấy từ MongoDB, ở đây dùng list cho gọn)
dealers_data = [
    {"id": 1, "full_name": "Best Cars LA", "city": "Los Angeles", "state": "CA", "st": "CA", "address": "123 Main St", "zip": "90001", "lat": 34.05, "long": -118.24},
    {"id": 2, "full_name": "Sunset Motors", "city": "San Francisco", "state": "CA", "st": "CA", "address": "45 Sunset Blvd", "zip": "94102", "lat": 37.77, "long": -122.41},
    {"id": 3, "full_name": "Downtown Autos", "city": "Chicago", "state": "IL", "st": "IL", "address": "78 Lake St", "zip": "60601", "lat": 41.88, "long": -87.63},
    {"id": 4, "full_name": "Wichita Auto Hub", "city": "Wichita", "state": "Kansas", "st": "KS", "address": "200 Main St", "zip": "67202", "lat": 37.68, "long": -97.33},
    {"id": 4, "full_name": "Wichita Auto Hub", "city": "Wichita", "state": "Kansas", "st": "KS", "address": "200 Main St", "zip": "67202", "lat": 37.68, "long": -97.33},
]

reviews_data = [
    {"id": 1, "dealership": 1, "name": "Alice Nguyen", "review": "Great service and friendly staff!", "purchase": True, "car_make": "Toyota", "car_model": "Camry", "car_year": 2022},
    {"id": 2, "dealership": 1, "name": "Bob Tran", "review": "Fast process, got my car in 2 days.", "purchase": True, "car_make": "Honda", "car_model": "Civic", "car_year": 2021},
    {"id": 3, "dealership": 2, "name": "Carol Le", "review": "Good prices but limited stock.", "purchase": False, "car_make": "Ford", "car_model": "Focus", "car_year": 2020},
]

def get_dealerships(request):
    return JsonResponse({"status": 200, "dealers": dealers_data})

def get_dealer_reviews(request, dealer_id):
    filtered = [r for r in reviews_data if r["dealership"] == dealer_id]
    return JsonResponse({"status": 200, "reviews": filtered})

def get_dealer_by_id(request, dealer_id):
    dealer = next((d for d in dealers_data if d["id"] == dealer_id), None)
    if dealer:
        return JsonResponse({"status": 200, "dealer": dealer})
    else:
        return JsonResponse({"status": 404, "message": "Dealer not found"})

def get_dealers_by_state(request, state):
    filtered = [d for d in dealers_data if d["state"].lower() == state.lower()]
    return JsonResponse({"status": 200, "dealers": filtered})

def get_dealers_by_state(request, state):
    filtered = [d for d in dealers_data if d["state"].lower() == state.lower()]
    return JsonResponse({"status": 200, "dealers": filtered})

# Data mẫu car makes và models tương ứng
car_makes_models = [
    {"CarMake": "Toyota", "CarModel": ["Camry", "Corolla", "RAV4"]},
    {"CarMake": "Honda", "CarModel": ["Civic", "Accord", "CR-V"]},
    {"CarMake": "Ford", "CarModel": ["Focus", "Mustang", "Explorer"]},
]

def get_cars(request):
    return JsonResponse({"CarModels": car_makes_models})

def analyze_review_sentiment(request, text):
    # Phân tích cảm xúc đơn giản dựa trên từ khóa (thay cho Watson NLU thật)
    positive_words = ["good", "great", "fantastic", "excellent", "friendly", "fast", "amazing"]
    negative_words = ["bad", "poor", "terrible", "slow", "rude", "worst"]

    text_lower = text.lower()
    if any(w in text_lower for w in positive_words):
        sentiment = "positive"
    elif any(w in text_lower for w in negative_words):
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return JsonResponse({"sentiment": {"document": {"label": sentiment}}})

from django.shortcuts import render

def index(request):
    return render(request, "index.html")

@csrf_exempt
def add_review(request):
    data = json.loads(request.body)
    new_review = {
        "id": len(reviews_data) + 1,
        "dealership": int(data.get("dealership")),
        "name": data.get("name"),
        "review": data.get("review"),
        "purchase": data.get("purchase"),
        "car_make": data.get("car_make"),
        "car_model": data.get("car_model"),
        "car_year": data.get("car_year"),
    }
    reviews_data.append(new_review)
    return JsonResponse({"status": 200, "message": "Review added"})
