import time
from collections import Counter

def pieces(s):
    """ yield all pieces for input line """
    for c in s[::-1]:
        if '1' <= c <= '9':
            yield suit, int(c)
        elif c != ' ':
            suit = c


def check(pc, n_sets, n_pairs, pairs=set()):
    """ check if piece counts in pc can be partitioned 
        into n_sets sets and n_pairs pairs (without repeated pairs) """
    if not pc:
        return True
        
    # the minimal element must be in a pair or a set
    elem = min(pc)
    
    # pair?
    if pc[elem] >= 2 and n_pairs and elem not in pairs:
        new_pc = pc - Counter({elem:2})
        if check(new_pc, n_sets, n_pairs-1, pairs|{elem}):
            return True

    # 3-of-a-kind?
    if pc[elem] >= 3 and n_sets:
        new_pc = pc - Counter({elem:3})
        if check(new_pc, n_sets-1, n_pairs, pairs):
            return True

    # sequence?
    suit, num = elem
    if suit != "z" and pc[suit, num+1] and pc[suit, num+2] and n_sets:
        new_pc = pc - Counter([elem, (suit, num+1), (suit, num+2)])
        if check(new_pc, n_sets-1, n_pairs, pairs):
            return True
            
    # nothing found
    return False
    

def check_complete_hand(line):
# Create piece counts from input
    pc = Counter(pieces(line))
    # check for conditions and print result
    if (
        check(pc, 4, 1)  # 4 sets and a pair 
        or check(pc, 0, 7)  # 7 pairs
        or set(pc) == set(pieces("19m19p19s1234567z"))  # kokushi musou
        ):
            print("TRUE")
    else:
            print("FALSE")

start_time = time.time()

check_complete_hand('222888m444p2277z 7z') # true
check_complete_hand('19m19p19s1234567z 6z') # true - kokushi
check_complete_hand('11m4477p8899s116z 6z') # true - 7 pair
check_complete_hand('122223567m3555p 4p') # true
check_complete_hand('1122223m111222z 4m') # true - complicated
check_complete_hand('19m139p19s123567z 4z') # false - not kokushi
check_complete_hand('11m4477p8899s666z 6z') # false - not 7 pairs
check_complete_hand('1122335778899m 1m') # false - not 7 pairs
check_complete_hand('234m45789p45688s 6p') # true
check_complete_hand('1133344566777m 9m') # false - not 7 pairs
check_complete_hand('1133344566777m 5m') # true
check_complete_hand('123345567789m3p 3p') # true

print("time used = %s seconds" % (time.time() - start_time))
