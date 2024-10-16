from django.http.response import HttpResponse
from django.http.request import HttpRequest


def hey_you(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"Hey, {name}!")

def age_in(request: HttpRequest, end: int, birthyear: int) -> HttpResponse:
    return HttpResponse(f"{end - birthyear}")

def order_total(request: HttpRequest, burgers: int, fries: int, drinks: int) -> HttpResponse:
    total = burgers * 4.50 + fries * 1.5 + drinks * 1
    return HttpResponse(f'${total}')