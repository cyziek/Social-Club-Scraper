
def get_headers():
    with open("request/bearer.txt", 'r') as file:
        bearer = file.readline()
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Origin': 'https://socialclub.rockstargames.com',
        'Pragma': 'no-cache',
        'Referer': 'https://socialclub.rockstargames.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'authorization': f'Bearer {bearer}',
        'baggage': 'sentry-environment=prod,sentry-release=2024-08-26dif_prod.sc,sentry-public_key=9c63ab4e6cf94378a829ec7518e1eaf6,sentry-trace_id=fa23d26506bc47b78163f5151d076744,sentry-sample_rate=0.0025,sentry-transaction=%2Fcrew%2F%3AcrewName%2F%3AcrewId%3F,sentry-sampled=false',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sentry-trace': 'fa23d26506bc47b78163f5151d076744-b8eb889318a77c33-0',
        'x-cache-ver': '0',
        'x-lang': 'en-US',
        'x-requested-with': 'XMLHttpRequest',
    }

    return headers
