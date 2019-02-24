def twoStrings(s1, s2):
    seed = ""
    search = ""
    srch_dict = dict()
    if len(s1) > len(s2):
        seed = s2
        search = s1
    else:
        seed = s1
        search = s2
    for ch in seed:
        if ch not in srch_dict:
            srch_dict[ch] = 1
    for ch in search:
        if ch in srch_dict:
            return "YES"
    return "NO"
if __name__ == '__main__':
    print(twoStrings("hi", "world"))