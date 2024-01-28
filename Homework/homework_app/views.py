import datetime
import logging
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
import pytz
# Create your views here.
logger = logging.getLogger(__name__)


def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django сайт!</h1>
    <p>Это сайт-домашка.</p>
    """
    cur_time = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime("%Y-%m-%d %H:%M:%S")
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f'{cur_time} - homepage')
    return HttpResponse(html)


def about(request):
    timezone.activate('Europe/Moscow')
    html = """
    <h2>Обо мне</h2>
    <p>Привет, я Бурлаков Валерий, студент GeekBrains, пишу домашку по Django.</p>
    """
    cur_time = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime("%Y-%m-%d %H:%M:%S")
    # current_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f'{cur_time} - about us page')
    return HttpResponse(html)


