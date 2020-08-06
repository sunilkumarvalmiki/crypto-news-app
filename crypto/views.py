from django.shortcuts import render


def home(request):
    import requests
    import json

    # grab crypto price
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    # grab crypto news
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        import requests
        import json
        search = request.POST['search']
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + search + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'search': search, 'crypto': crypto})
    else:
        notfound = "enter a crypto currency symbol in the above search . . ."
        return render(request, 'prices.html', {'notfound': notfound})
