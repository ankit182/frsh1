from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from bs4 import BeautifulSoup
# from requests_futures.sessions import FuturesSession as async

import simplejson
import wikipedia
import grequests
import requests
import random
import json
import sys
import re
import os

base_dir = os.path.dirname(os.path.dirname(__file__))

def main_pg(request):
    context = {}
    return render(request, 'index.html', context)

# def err404(request):
#     return render(request,'error/index.html',{})
# def sitemap(request, param):
#     context = {}
#     url = "sitemap/" + param
#     return render(request, url, {}, content_type="application/xml")