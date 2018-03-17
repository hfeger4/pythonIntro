# print(dir())
#
# for m in dir(__builtins__):
#     print(m)

import shelve

# for obj in dir(shelve.Shelf):
#     if obj[0] != "_":
#         print(obj)

# help(shelve)

import webbrowser

# webbrowser.open("www.howiefeger.com")

help(webbrowser)

chrome = webbrowser.get('google-chrome %s')
chrome.open("www.howiefeger.com")

for i in range(10):
    print(1,2,3,4,5,6,7,8,9, sep=": ", end=" ")

