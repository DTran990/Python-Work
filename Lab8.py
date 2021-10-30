# YOUR NAME David Tran  
# YOUR STUDENT NUMBER 500890757

# ***INSTRUCTIONS***
# Failure to follow the instructions will result in a mark of 0 on the lab, with no exceptions
# Do not edit the code ANYWHERE other than where indicated
# Submit your file with the name Lab8.py

# You are implementing insertion into a hash table with 3 different algorithms for collision handling:
# - Separate Chainging
# - Linear Probing
# - Double Hashing

# Use the functions provided for hashing

# Complete the following functions
def insertWithSeparateChaining(key, ht):
    # Complete this function for insertion with separate chaining
    moddedval = key%11
    ht[moddedval].append(key)
def insertWithLinearProbing(key, ht):
    # Complete this function for insertion with linear probing
    probe = 0
    while probe <= key:
        hmod = (key+probe)%11
        if not ht[hmod]:
            ht[hmod] = key
            break
        probe+=1


def insertWithDoubleHashing(key, ht):
    # Complete this function for insertion with double hashing
    firsthash = hashFunction(key)
    secondhash = secondaryHashFunction(key)
    total = firsthash + secondhash
    if not ht[firsthash]:
        ht[firsthash] = key
    else:
        while True:
            if total <= 10:
                if not ht[total]:
                    ht[total] = key
                    break
                else:
                    total+=secondhash
            else:
                total-=11

# DO NOT EDIT THE CODE BELOW THIS LINE

def hashFunction(key):
    return (3 * key + 5) % 11

def secondaryHashFunction(key):
    return 7 - (key % 7)

def printHashTable(ht):
    print("Index\tValue")
    print("---------------------")
    for i in range(len(ht)):
        print(str(i) + "\t" + str(ht[i]))
    print("")
    print("")

keys = [12, 44 ,13, 88, 23,94,11,39,20,16,5]

ht1 = [ [] for _ in range(11) ]
for key in keys:
    insertWithSeparateChaining(key, ht1)

ht2 = [None] * 11
for key in keys:
    insertWithLinearProbing(key, ht2)

ht3 = [None] * 11
for key in keys:
    insertWithDoubleHashing(key, ht3)

print("Hash Table w/ Separate Chaining")
printHashTable(ht1)
print("Hash Table w/ Linear Probing")
printHashTable(ht2)
print("Hash Table w/ Double Hashing")
printHashTable(ht3)