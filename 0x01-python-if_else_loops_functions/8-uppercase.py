def uppercase(str):
    new_str = ""
    for i in str:
        c = ord(i):
        if c in range(65, 91, 1):
            new_str += chr(c)
        elif c in range(97, 123, 1):
            new_str += chr(c -32)
        else:
            new_str += chr(c)
    print("{}".format(new_str))
