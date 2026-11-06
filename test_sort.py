import random
import string
from sort import sort1st

# Setting: we're sorting (string, int) tuples based only on the first (string) component.
# Thus, we can have objects in the list tht are equivalent (from the sort's perspective)
# that actually differ on their data, and are not "equal" to one another.

def test_unsorted_with_duplicate_strings():
    data = [("bob", 2), ("alice", 5), ("bob", 1), ("alice", 3)]
    
    assert sort1st(data) == [("alice", 3), ("alice", 5), ("bob", 1), ("bob", 2)]
    # Would we also be OK with this next one?
    # assert sort(data) == [("alice", 5), ("alice", 3), ("bob", 1), ("bob", 2)]
    # If no, then we have an added property (stability) to think about. 
    # If yes, then this test case is specialized (i.e., overfit) to our implementation.

def generateRandomString(maxLen: int = 5):
    return ''.join(random.choices(string.ascii_letters, k=random.randint(1, maxLen)))

def generateRandomList():
    return [(generateRandomString(), random.randint(0, 10)) for _ in range(random.randint(0, 5))]

def test_sorted_correct_random():
    '''output is a sorted version of input'''
    for counter in range(1_000_000):
        input = generateRandomList()
        output = sort1st(input)
        assert correctSorted(input, output)
    pass

def test_sorted_consistent():
    '''Is our sort deterministic, i.e., returns the same result always for the 
       same input? It's very hard, if not impossible, to test this perfectly. 
       For now, let's just check consecutive invocations.'''
    for counter in range(1_000_000):
        input = generateRandomList()
        output1 = sort1st(input)
        output2 = sort1st(input)
        assert output1 == output2 
    pass

def correctSorted(input: list, output: list):
    ###### PROPERTY: output is sorted: n+1th ele >= nth ele
    for i in range(len(output) - 1):
        if output[i][0] > output[i+1][0]: return False
    
    # length of output = length of input 
    if len(input) != len(output): return False
    
    ###### PROPERTY: everything in input is in the output 
    ######      AND  everything in output is in the input 
    
    # NOT this, which doesn't account for, e.g., [2, 2, 3, 1] vs. [2, 3, 3, 1]
    #if len(input) != len(output):
    #    return False

    # Instead, check that output is a _permutation_ of the input.
    for x in input:
        if input.count(x) != output.count(x): return False
    
    # Amusingly, I was playing with Claude on this, and it suggested:
    # if sorted(input) != sorted(output): return False
    # It's worth asking yourself why I didn't like that version.


    return True


# [2, 3, 1] in [1, 2, 3]
# [2, 2, 3, 1] in [1, 2, 3]  # caught by the length check
# [2, 2, 3, 1] in [2, 3, 3, 1] # passes both weak for loops 
