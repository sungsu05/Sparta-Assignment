# # https://jsonplaceholder.typicode.com/posts
# # pip install requests
# import requests
#
# # get
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(response.text)
#
# # post
# data = {'title': 'foo', 'body': 'bar', 'userId': 1}
# response = requests.post('https://jsonplaceholder.typicode.com/posts', data=data)
# print(response.text)
#
#
# # put,delete
# data = {'title': 'foo', 'body': 'bar', 'userId': 1}
# response = requests.put('https://jsonplaceholder.typicode.com/posts/1', data=data)
# print(response.text)
#
# response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
# print(response.text)



# c

# curl https://jsonplaceholder.typicode.com/posts
# curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
# curl -X PUT -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts/1
# curl -X DELETE https://jsonplaceholder.typicode.com/posts/1