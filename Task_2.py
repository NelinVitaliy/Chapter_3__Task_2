
words = input('Enter something: ')
words = words.split()
words.sort(key=len)
# print(type(words))
words = ' '.join(words)
# print(type(words))
print(words)


# def f(x):
# 	return len(x)
# a = ["aaa", "knkn", "nnnnj"]


# a.sort(key=lambda x: len(x))
# a.sort(key=f)
# print(a)


# a = (sorted(input('Enter something: ').split(), key = len))
# a = ' '.join(a)
# print(a)
