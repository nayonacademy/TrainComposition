from django.http.response import HttpResponse
from django.shortcuts import render
import json, requests
# Create your views here.

def index(request):
    url = 'https://rata.digitraffic.fi/api/v1/live-trains?station=SLO'
    resp = requests.get(url=url)
    data = json.loads(resp.text)
    date = '2017-05-02'
    finaldata = {}
    case_list = []
    for i in data:
        tranno = i['trainNumber']
        url1 = 'https://rata.digitraffic.fi/api/v1/compositions/'+str(tranno)+'?departure_date='+date
        resp1 = requests.get(url=url1)
        data1 = json.loads(resp1.text)
        try:
            wagon = []
            case = {'trainNumber' : data1['trainNumber'],
                    'trainType': data1['trainNumber'],
                    'stationShortCode': data1['journeySections'][0]['beginTimeTableRow']['stationShortCode'],
                    'stationShortCode2' : data1['journeySections'][0]['endTimeTableRow']['stationShortCode'],
                    'locomotiveType': data1['journeySections'][0]['locomotives'][0]['locomotiveType'],
                    'wagons' : wagon,
                    'maximumSpeed': data1['journeySections'][0]['maximumSpeed'],
                    'totalLength': data1['journeySections'][0]['totalLength']
                    }
            case_list.append(case)

            try:
                for w in data1['journeySections'][0]['wagons']:
                    print(w['wagonType'])
                    wgn = {'wagonType': w['wagonType']}
                    wagon.append(wgn)
            except:
                pass
        except:
            pass
    print(case_list)
    context = {
        'data': data,
        'finaldata': case_list
    }
    return render(request, 'home.html', context)