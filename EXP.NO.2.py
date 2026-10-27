def accepts_string(s):
    state = 0

    for ch in s:
        if ch == 'a':
            state = 1
        elif ch == 'b':
            if state == 1:
                state = 2
            else:
                state = 0
        else:
            return False

    return state == 2

strings = ["ab", "aab", "bab", "abb", "aba", "ba", "abc"]
for s in strings:
    if accepts_string(s):
        print(s, "-> Accepted")
    else:
        print(s, "-> Rejected")
