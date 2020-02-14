from django.shortcuts import render

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_c66fd30cc0bb46ffb5b74572eb6ed472")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api':api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})

    # pk_c66fd30cc0bb46ffb5b74572eb6ed472
    # https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_c66fd30cc0bb46ffb5b74572eb6ed472
    

def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    return render(request, 'add_stock.html', {})