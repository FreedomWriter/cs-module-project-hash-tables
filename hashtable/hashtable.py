class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity >= MIN_CAPACITY:
            self.capacity = capacity
        else:
            self.capacity = MIN_CAPACITY

        self.hash_table_list = [HashTableEntry(None, None)] * self.capacity
        self.num_of_els = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.hash_table_list)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        slots = self.get_num_slots()
        return self.num_of_els / slots


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here 

        # algorithm fnv-1 is
        # hash := FNV_offset_basis do

        # for each byte_of_data to be hashed
        #     hash := hash × FNV_prime
        #     hash := hash XOR byte_of_data

        # return hash
        
        offset_basis = 14695981039346656037
        FNV_prime =  1099511628211
        my_hash = offset_basis

        for byte_of_data in key:
            my_hash = my_hash * FNV_prime
            my_hash = my_hash ^ ord(byte_of_data)
        
        return my_hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)
        cur_node = self.hash_table_list[idx]
        traversing = True
        self.num_of_els += 1


        while traversing: 
            # does the cur_node have a key?
            if cur_node.key:
                # is the cur_node's key equal to the key being passed?
                if cur_node.key != key:
                    # is there a next node?
                    if cur_node.next:
                        cur_node = cur_node.next
                    # no next - create the new entry
                    else:
                        cur_node.next = HashTableEntry(key, value)
                        traversing = False
                # if the key's are the same, overwrite the value
                else:
                    cur_node.value = value
                    traversing = False
            # if the cur_node does not have a key
            else:
                cur_node.key = key
                cur_node.value = value
                traversing = False

        # load_factor = self.get_load_factor()
        # print(load_factor)
        # if load_factor > .7:
        #     return self.resize(self.capacity * 2)
        # elif load_factor < .2:
        #     return self.resize(self.capacity / 2)
      

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)
        cur_node = self.hash_table_list[idx]
        traversing = True
        self.num_of_els -= 1

        while traversing: 
            if cur_node.key:
                if cur_node.key == key:
                    cur_node.value = None
                    return None
                else:
                    if cur_node.next:
                        cur_node = cur_node.next
                    else:
                        return None
            else: 
                return f"Warning: No {key} found in hash table"


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)
        cur_node = self.hash_table_list[idx]
        traversing = True

        while traversing:
            if cur_node.key:
                if cur_node.key == key:
                    return cur_node.value
                else:
                    cur_node = cur_node.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here - O(n)
        old_arr = self.hash_table_list
        self.hash_table_list = [HashTableEntry(None, None)] * int(new_capacity)

        for el in old_arr:
            self.put(el.key, el.value)
            cur_node = el
            
            while cur_node:
                self.put(cur_node.key, cur_node.value)
                cur_node = cur_node.next
             
            ## Verbose implementation
            # if el.next:
            #     traversing = True
            #     cur_node = el.next
            #     while traversing:
            #         self.put(cur_node.key, cur_node.value)
            #         if cur_node.next:
            #             cur_node = cur_node.next
            #         else:
            #             traversing = False
                




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
