import requests

def print_ip_info(ip=''):
    """Данная функция печатает информацию об указанном IP. Еси параметр ip пустой, то выведется информация о вашем текущем ip."""
    url = f'http://ip-api.com/json/{ip}'
    params = {
        'fields': 'status,message,country,countryCode,region,regionName,city,timezone,query',
        'lang': 'ru'
    }
    request = requests.get(url, params=params)
    if request.status_code != 200:
        print('Произошла ошибка во время запроса по адресу' + request.url + ', код' + str(request.status_code))
    else:
        response = request.json()
        print(f'Информация об IP {response['query']}\nСтрана: {response['country']} ({response['countryCode']})\nРегион: {response['regionName']}\n'
              f'Город: {response['city']}\nЧасовой пояс: {response['timezone']}')

print_ip_info()
