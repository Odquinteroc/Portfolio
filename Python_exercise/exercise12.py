x = ['HA NOI', 'THAI BINH', 'LANG SON', 'DA NANG']
def get_first(string):
    return string.split()[0]
list_functions = [get_first, str.lower]
a=[list_functions[1](ss) for ss in [list_functions[0](s) for s in x]]
print(a)