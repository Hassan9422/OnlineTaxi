import requests
import login_requests

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

# create_one_user
# new = {"name": "hassan", "phone_number": 1234567892, "address": "urmia1", "email": "klav@gmail.com", "password": "password1"}
# print(requests.post(f'{hostname}users', json=new).json())

# get_all_users
# remember that query parameters come after ? mark in the URL like below. also we can use as many queriesas we want, we have to just put
# "&" to separate them. also if we wanna type space, we have to type "%20" in the URL, like below:
# for x in requests.get(f'{hostname}users?search=new%20title&limit=3&skip=0', headers={'Authorization': f"Bearer {access_token}"}).json():
# for x in requests.get(f'{hostname}users', headers={'Authorization': f"Bearer {access_token}"}).json():
#     print(x)
# for x in requests.get(f'{hostname}users').json():
#     print(x)

# get_one_user
# print(requests.get(f'{hostname}users/2?search=new%20title&limit=5&skip=3').json())
# print(requests.get(f'{hostname}users/8', headers={'Authorization': f"Bearer {access_token}"}).json())

# update_one_user
# user = {"name": "hassan", "phone_number": 1234567895, "address": "Urmia77", "email": "klav@gmail.com", "password": "password1"}
# print(requests.put(f'{hostname}users/6', json=user,
#                    headers={'Authorization': f"Bearer {access_token}"}).json())

# delete_one_user
# print(requests.delete(f'{hostname}users/8', headers={'Authorization': f"Bearer {access_token}"}).status_code)

# Voting on a product
# vote = requests.post(f'{hostname}votes', json={'product_id': 13, 'dir': 1}, headers={'Authorization': f"Bearer {access_token}"})
# print(vote.json())
# print(f"status_code= {vote.status_code}")


