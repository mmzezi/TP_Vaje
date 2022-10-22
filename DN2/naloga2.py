our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)
x_our_list = our_list[4]
#print(x_our_list)
del our_list[4] #odstranimo element iz tabele
#print(our_list)
our_dict.update({'d':x_our_list}) #vrednost ključa d zamenjam z vrednostjo x_our_list
#print(our_dict)
new_tuple = list(our_dict.values()) #v python3 je potrebno dodati še "list" drugače shrani kot string
print(new_tuple)
print(our_tuple)

if new_tuple == our_tuple:
    print("Touple-a sta enaka")
