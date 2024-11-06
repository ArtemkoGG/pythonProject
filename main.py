def lest(f):
    if any(len(i) >= 5 for i in f):
        print("True")
    else:
        print("False")


    if all(type(i) == str for i in f):
        print("All are str")
    else:
        print("All not str")


    if all(i.isalpha() for i in f):
        print("All are in alphabet")
    else:
        print("Not All are in alphabet")


lest(["Hello", "Bye", "If"])
