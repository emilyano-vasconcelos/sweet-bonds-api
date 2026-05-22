from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import PlayerProfile

import json


def _get_json_body(request):
    try:
        return json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return None


@csrf_exempt
def register(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Use POST."}, status=405)

    data = _get_json_body(request)
    if data is None:
        return JsonResponse({"success": False, "error": "JSON inválido."}, status=400)

    username = (data.get("username") or "").strip()
    password = data.get("password") or ""

    if not username or not password:
        return JsonResponse({"success": False, "error": "Usuário e senha são obrigatórios."}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"success": False, "error": "Esse usuário já existe."}, status=400)

    user = User.objects.create_user(username=username, password=password)
    PlayerProfile.objects.get_or_create(user=user)

    return JsonResponse({"success": True, "message": "Usuário registrado com sucesso."})


@csrf_exempt
def login(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Use POST."}, status=405)

    data = _get_json_body(request)
    if data is None:
        return JsonResponse({"success": False, "error": "JSON inválido."}, status=400)

    username = (data.get("username") or "").strip()
    password = data.get("password") or ""

    if not username or not password:
        return JsonResponse({"success": False, "error": "Usuário e senha são obrigatórios."}, status=400)

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"success": False, "error": "Usuário ou senha incorretos."}, status=401)

    PlayerProfile.objects.get_or_create(user=user)
    return JsonResponse({"success": True, "username": user.username})


@csrf_exempt
def update_score(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Use POST."}, status=405)

    data = _get_json_body(request)
    if data is None:
        return JsonResponse({"success": False, "error": "JSON inválido."}, status=400)

    username = (data.get("username") or "").strip()

    try:
        score = int(data.get("score", 0))
    except (TypeError, ValueError):
        return JsonResponse({"success": False, "error": "Score inválido."}, status=400)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({"success": False, "error": "Usuário não encontrado."}, status=404)

    profile, _ = PlayerProfile.objects.get_or_create(user=user)
    profile.score = max(profile.score, score)
    profile.save()

    return JsonResponse({"success": True, "updated": True, "score": profile.score})


@csrf_exempt
def ranking(request):
    if request.method != "GET":
        return JsonResponse({"success": False, "error": "Use GET."}, status=405)

    players = PlayerProfile.objects.select_related("user").order_by("-score", "user__username")[:10]

    data = [
        {
            "username": player.user.username,
            "score": player.score,
        }
        for player in players
    ]

    return JsonResponse(data, safe=False)
