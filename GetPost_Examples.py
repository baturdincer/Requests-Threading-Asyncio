import requests
import json

#GET
# get_url= "https://jsonplaceholder.typicode.com/todos/2"
# get_response= requests.get(get_url)
# print(get_response.json())

#POST
post_url= "https://jsonplaceholder.typicode.com/todos"
todo_item={"userId":2, "title":"ekmek", "completed":True}
#OPTIONAL HEADER
headers={"Content-Type":"application/json"}
post_response=requests.post(post_url, data=json.dumps(todo_item), headers=headers)
print(post_response.json())
# print(json.dumps(todo_item))