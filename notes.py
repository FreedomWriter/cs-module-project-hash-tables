# 

my_arr = ["hi", "world", "how", "are", "you", "lorem", "ipsum", "set"]

# o(n) search - best case O(log n) if sorted and can use binary
def find_el(arr, el):
    for item in arr:
        if item == el:
            return True
    return False


## Write a function that will take a string and return a number

def len_hash(s):
    return len(s)
## Cons
# A lot of collisions ^^

## Pros
# Fast
# Readable
# Deterministic

# add up the ASCII or unicode

## Cons
# A lot of collisions ^^

## Pros
# Fast
# Readable
# Deterministic

def asciii_hash(s):
    for letter in s:
        # ord() gives the ascii code for a given letter
        val = ord(letter)
        total += val

# use .encode() UTF-8 (less American centric in comparison to ascii)

def UTF8_hash(s):
    utf_bytes = s.encode()
    total = 0
    for b in utf_bytes:
        total += b
    return total

# A hash function: takes, string, gives back number
## operate on the bytes that make up a string
## Needs to be Deterministic

# To imporve our hash functions, me make the output more unique!
## SHA256

## Hash function + arr!!
## hash function give us back some big number
### how to map the output of our hash function to an index in an array?

my_arr2 = [None] * 20


# PUT
our_hash = UTF8_hash('supercalifragilisticexpialidocious') ## 364
idx = our_hash % len(my_arr2) ## 364
my_arr2[idx] = 'Mary Poppins' # gives an index error ( 364 is greater than the index capacity, 20)

print(my_arr2)

