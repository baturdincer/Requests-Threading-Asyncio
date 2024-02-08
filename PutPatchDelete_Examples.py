import requests

url= "https://jsonplaceholder.typicode.com/todos/15"
# get_response=requests.get(url)
# print(get_response.json())

#PUT
todo_item_15={"userId": 2, "title":"Köfte ekmek", "completed": False}
# put_response= requests.put(url, todo_item_15)
# print(put_response.json())

#PATCH
todo_item_15_patch= {"title": "sucuk ekmek"}
# patch_response= requests.patch(url,todo_item_15_patch)
# print(patch_response.json())

#DELETE
delete_response= requests.delete(url)
print(delete_response.json())
print(delete_response.status_code)