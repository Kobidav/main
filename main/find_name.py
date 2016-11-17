d = dict.fromkeys(['aa bb', 'cc dd', 'ee jj', 'uu qq',
                   'oo aa', 'ff jj', 'aa uu'], 100)
f = ['aa', 'jj', 'cc', 'uu', 'ff']
k = ['bb', 'dd', 'ee', 'qq', 'uu']


def find_name(image, names, sonames):
    list_so = []
    for key in image.keys():
        for so in sonames:
            if so in key:
                list_so.append(key)
                print(so, "!in ", key)
        if len(list_so) > 1:
            print(list_so)
            for in_list in list_so:
                for na in names:
                    if na in in_list:
                        print(na, "!in ", in_list)


find_name(d, f, k)
