
import requests
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='log.txt', filemode='a')

def getdata():
    url = 'https://jsonplaceholder.typicode.com/users'
    try:
        response= requests.get(url)
        logging.info(f"GET {url} - Status Code: {response.status_code}")
        if response.status_code == 200:
            for name in response.json():
                print(name['name'])
            else:
                logging.warning(f"GET {url} - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(e)
getdata()

def post_data():
    url = 'https://jsonplaceholder.typicode.com/users'
    my_data = {
        'id':234536,
        'name': 'Denis',
        'username': 'rain',
        'email': "denis@.mail.ua"
    }

    try:
        response = requests.post(url, json=my_data)
        logging.info(f"POST {url} - Status Code: {response.status_code}")
        if response.status_code == 201:
            logging.info(f"Added new user: {response.json()['name']}")
        else:
            logging.warning(f"POST {url} - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(e)
post_data()

# def get_posts():
#     params={'userId': 1}
#     headers = {"Accept" :'application/json'}
#     url = 'https://jsonplaceholder.typicode.com/posts'
#     try:
#         response = requests.get(url, params=params, headers=headers)
#
#         print(response.status_code)
#         posts = response.json()
#         for post in posts:
#             print(post['title'])
#         print(response.headers["Content-Type"])
#     except requests.exceptions.RequestException as e:
#         print(e)
# get_posts()

