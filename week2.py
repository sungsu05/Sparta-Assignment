phone_book = {"son": "123-456", "son1": "234-456", "son2": "345-456"}


def search():
    name = yield
    while True:
        if name in phone_book:
            phone_number = phone_book[name]
        else:
            phone_number = "등록된 번호가 없습니다."
        name = yield phone_number


search_coroutine = search()
next(search_coroutine)

result = search_coroutine.send("son")
print(result)

result = search_coroutine.send("son1")
print(result)

result = search_coroutine.send("test")
print(result)