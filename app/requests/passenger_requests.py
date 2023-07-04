import requests
import sys
import login_requests
# from pathlib import Path

# sys.path.append(Path(f"{__file__}/../..").resolve().as_posix())

while True:
    try:
        # env = input("Please specify the environment you would like to use:(D: Development/ P: Production")
        env = 'd'  # line above is asking the type of environment. but we have set it to development temporarily.
        if env.lower() == 'd':
            hostname = 'http://127.0.0.1:8000/'  # your local system hostname.
            break
        elif env.lower() == 'p':
            hostname = 'http://127.0.0.1:8000/'  # this is temporary. you should enter the hostname of your production environment here.
            break
        else:
            raise ValueError
    except ValueError:
        print("Please enter 'D' for Development and 'P' for Production.")

# with open('token.csv') as file1:
#     reader = csv.DictReader(file1)
#     for row in reader:
#         t1, jwt_token = row['time'], row['token']
#
# if t1 == 0:
#     t1, jwt_token = time.time(), login_reqs.jwt_token
#
#     with open('token.csv', 'w') as file1:
#         writer = csv.DictWriter(file1, fieldnames=['time', 'token'])
#         writer.writeheader()
#         writer.writerow({'time': t1, 'jwt_token': jwt_token})
# else:
#     if time.time() - t1 > setting.access_token_expire_minutes:
#         t1, jwt_token = time.time(), login_reqs.jwt_token
#
#         with open('token.csv', 'w') as file1:
#             writer = csv.DictWriter(file1, fieldnames=['time', 'token'])
#             writer.writeheader()
#             writer.writerow({'time': t1, 'jwt_token': jwt_token})

access_token = login_requests.jwt_token['token']

# create_one_passenger
passenger = {'source': 'a', 'destination': 'b'}
print(requests.post(f'{hostname}passengers', json=passenger,
                    headers={'Authorization': f"Bearer {access_token}"}).json())
# print(requests.post(f'{hostname}passengers', json=product).json())

# get_all_products
# remember that query parameters come after ? mark in the URL like below. also we can use as many queries as we want, we have to just put
# "&" to separate them. also if we wanna type space, we have to type "%20" in the URL, like below:

# for x in requests.get(f'{hostname}passengers?search=new%20title&limit=3&skip=0', headers={'Authorization': f"Bearer {access_token}"}).json():

# for x in requests.get(f'{hostname}passengers', headers={'Authorization': f"Bearer {access_token}"}).json():
#     print(x)
# for x in requests.get(f'{hostname}passengers').json():
#     print(x)

# get_one_product print(requests.get(f'{hostname}passengers/2?search=new%20title&limit=5&skip=3', headers={'Authorization': f"Bearer {
# access_token}"}).json()) print(requests.get(f'{hostname}passengers/1').json())

# update_one_passenger
# product = {'name': 'cake', 'category': 'food', 'original_price': '1', 'discount': '0.3'}
# print(requests.put(f'{hostname}passengers/14', json=product,
#                    headers={'Authorization': f"Bearer {access_token}"}).json())

# delete_one_passenger
# print(requests.delete(f'{hostname}passengers/12', headers={'Authorization': f"Bearer {access_token}"}).status_code)

# Voting on a product
# vote = requests.post(f'{hostname}votes', json={'product_id': 13, 'dir': 1}, headers={'Authorization': f"Bearer {access_token}"})
# print(vote.json())
# print(f"status_code= {vote.status_code}")
