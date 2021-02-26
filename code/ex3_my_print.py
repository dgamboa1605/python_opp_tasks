def my_print(*text):
    return "".join([i + " - " for i in text])[:-2]

print(my_print("arg1", "arg2", "arg3", "arg5"))