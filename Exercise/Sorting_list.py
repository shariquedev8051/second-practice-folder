def list_cleaner(l):
    cleaned_list = []
    for element in l:
        if isinstance(element,list):
            l1 = list_cleaner(l=element)
            cleaned_list.extend(l1)
        else:
            cleaned_list.append(element)
    return cleaned_list

l = [1,4,[[9,7,8],[9,10,3,5],8],5,6,[8,5,89,7],7]
print(list_cleaner(l))
