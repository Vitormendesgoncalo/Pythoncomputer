def Up():
    print("Up")
def Down():
    print("Up")
def Right():
    print("Up")
def Left():
    print("Up")
while True:
    Dictionary = {
        0: Up,
        1: Down,
        2: Right,
        3: Left,
    }
    Dictionary = Dictionary.get(int(input("Enter with 0 Up or 1 Down or 2 Right or 3 Left:")))
    Dictionary()