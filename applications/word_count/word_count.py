

def word_count(s):
    # Your code here
    obj = {}
    no_punc = s
    # initializing punctuations string  
    punc = r'":;,.-+=/\\|[]{}()*^&'
     
    for ele in no_punc:  
        if ele in punc:  
            no_punc = no_punc.replace(ele, "")
    
    my_list = no_punc.split()
    for word in my_list:
        if not word.lower() in obj:
            obj[word.lower()] = 0
        obj[word.lower()] += 1
    return obj
            

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))