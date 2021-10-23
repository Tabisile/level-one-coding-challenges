def longest_strings(list1):
    p = 0
    s = []
    for item in  list1:
        if len(item) > p:
           s = [item]
           p = len(item)
        elif len(item) == p:
           s.append(item)
    print(s)
