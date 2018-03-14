# print((range(0,5,2)) == range(0,6,2))
#
# r = range(100)
# print(r)
#
# for i in r[::-2]:
#     print(i)
#
# print('=' * 20)
#
# for i in range(99,0,-2):
#     print(i)
#
# print(range(100)[::-2] == range(99,0,-2))
#
# # range(100,0,-2) doesnt make sense, you start at 0 and subtract until you hit 100? Not possible.
#
# hello = "Hello world"
# print(hello[::-1])
#
# r = range(10)
# for i in r[::-1]:
#     print(i)
#

o = range(0,100,4)
print(list(o))
p = o[::5]
print(list(p))