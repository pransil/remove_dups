#remove_dups.py - a little practice code

in_str = 'abccddddkiuiiukggerhwhheaz'

#def make_hash(str):


def remove_dups(in_str):
    #hash_t = make_hash(in_str)

    out_str = ''
    for char in in_str:
        if char not in out_str:
            out_str += char

    print("in_str = ", in_str)
    print("out_str = ", out_str)
    return out_str

remove_dups(in_str)

ss = set()
ss.add(1)
ss.add(2)
ss.add(2)

print(ss)
print(str(ss))