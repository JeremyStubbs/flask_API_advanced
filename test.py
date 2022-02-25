from requests import put, get
put('http://127.0.0.1:5000/todos/milk', data={'task': 'Remember the milk'}).json()

y = get('http://127.0.0.1:5000/todos').json()
print(y)
x = get('http://127.0.0.1:5000/todos/milk').json()
print(x)
