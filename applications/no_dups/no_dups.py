def no_dups(s):
    # Your code here
    obj = {}
    my_list = s.split()
    test_list = set(list(s.split()))
    for word in my_list:
        if not word in obj:
            obj[word]= 0
        obj[word] += 1
    new_list = list(obj.keys())

    result =""
    for word in new_list:
        if word in test_list:
            result += f"{word} "
    return result.rstrip()
        
    




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))