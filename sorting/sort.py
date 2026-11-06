
def sort1st(items: list[tuple[str, int]]) -> list[tuple[str,int]]:
    '''Rather than doing something complicated, we'll just use Python's 
       built-in sort, and give it a key definition: extract only the 
       first (string) component. This is a great application of some of the 
       FP principles we've learned.'''
    return sorted(items, key=lambda t: t[0])

def sort_from_class(items: list):
    '''An implementation under test. 
       Supposedly, this sorts a list of (string,int) tuples in ascending order.
       It is "generic" in that it can sort lists of anything... provided that 
       the "anything" objects implement a notion of greater-than. 
       Tuples implement a lexical ordering: compare the first component, then the 
       second, and so on. Thus, this version of the sort doesn't really show the 
       idea of two different elements being sorted the same. See rewrite above.'''
    result = list(items)
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result
