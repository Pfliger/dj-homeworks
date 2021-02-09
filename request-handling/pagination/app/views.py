from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from urllib.parse import urlencode
from django.conf import settings
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse(bus_stations))

def get_paginator():
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as file:
        result = []
        reader = csv.DictReader(file)
        for row in reader:
            result.append(row)
    paginator = Paginator(result, settings.PAGINATION_RECORDS_PER_PAGE)
    return paginator
paginator = get_paginator()



def bus_stations(request):
    current_page_number = request.GET.get('page', '1')
    current_page = paginator.get_page(current_page_number)
    prev_page_url, next_page_url = None, None
    if current_page.has_previous():
        prev_page_url = f'{reverse(bus_stations)}?{urlencode({"page": current_page.previous_page_number()})}'
    if current_page.next_page_number() :
        next_page_url = f'{reverse(bus_stations)}?{urlencode({"page": current_page.next_page_number()})}'

    return render(request, 'index.html', context={
        'bus_stations': current_page.object_list,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

