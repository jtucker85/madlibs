def madlib():
    adj = input("Adjective: ")
    name = input("Name: ")
    bpart = input("Body part: ")
    item = input("Item: ")


    madlib = f"The problem with farming is that it's really quite {adj}. For example, I once worked with {name} and they got their hand stuck in \
    a cow's {bpart}. Unfortunately it had to be amputated, but they didn't mind because they got a free {item}."

    print(madlib)