def split_parity(lst):
    curr_index = 0
    num_evens = 0
    while curr_index < len(lst):
        if lst[curr_index] % 2 == 0:
            lst.append(lst.pop(curr_index))
            num_evens += 1
        if num_evens == (len(lst)-curr_index):
            return lst
        else:
            curr_index+=1
    return lst
