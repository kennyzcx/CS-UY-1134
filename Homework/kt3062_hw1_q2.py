#part a
def shift_a(lst, k):
    for i in range(k):
        lst.append(lst.pop(0))
    return lst

#part b
def shift_b(lst, k, direction="left"):
    if direction == "left":
        for i in range(k):
            lst.append(lst.pop(0))
    elif direction == "right":
        for i in range(k):
            lst.insert(0,lst.pop(-1))
    return lst
  
