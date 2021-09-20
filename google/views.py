from django.shortcuts import render, redirect

import requests

from bs4 import BeautifulSoup as bs

from xml.etree import ElementTree

from django.utils.translation import gettext

# Create your views here.



def index(request):
    return render(request, 'google/index.html')


def search(request):

    if request.method == "POST":

        search = request.POST.get('search', str)

        url = f"https://www.ask.com/web?q={search}"

        res = requests.get(url)

        soup = bs(res.text,'lxml')


        result_listings = soup.find_all('div',{'class':'PartialSearchResults-item'})

        final_result = []

        for result in result_listings:

            result_title = result.find(class_='PartialSearchReasults-item-title')

            if result_title is not None:

                result_title = result_title.text
            else:
                result_title = None

            result_url = result.find('a').get('href')

            result_desc = result.find(class_='PartialSearchResults-item-abstract')

            if result_desc is not None:
                result_desc = result_desc.text
            else:
                result_desc = None

            final_result.append((result_title, result_url, result_desc))

        context= {'final_result':final_result}

        return render(request, 'google/search.html', context)
    else:
        return render(request, 'google/search.html')