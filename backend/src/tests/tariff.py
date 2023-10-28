import requests

base_url = "http://127.0.0.1:8080/api"


def test1():
    res = requests.get(f'{base_url}/tariff/1')

    print(res.status_code)
    print(res.content)


def test3():
    res = requests.get(f'{base_url}/tariffs')

    print(res.status_code)
    print(res.content)


def test2():
    res = requests.post(f'{base_url}/tariff',
                        json={
                            'name': 'eqweqw',
                            'price': 10,
                            'description': 'tariffsadqweqw'
                        })

    print(res.status_code)
    print(res.content)


if __name__ == '__main__':
    test1()
