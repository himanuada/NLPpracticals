def FA(s):
    size = 0
    # scan complete string and make sure that it contains only 'a' & 'b'
    for i in s:
        if i == 'a' or i == 'b':
            size += 1
        else:
            return "Rejected"
    
    # After checking that it contains only 'a' & 'b'
    # check its length; it should be at least 3
    if size >= 3:
        # check the last 3 elements
        if s[size-3] == 'b':
            if s[size-2] == 'b':
                if s[size-1] == 'a':
                    return "Accepted"  # if all 3 ifs are true
                return "Rejected"  # else of 3rd if
            return "Rejected"  # else of 2nd if
        return "Rejected"  # else of 1st if
    return "Rejected"


inputs = ['bba', 'ababbba', 'abba', 'abb', 'baba', 'bbb', '']
for i in inputs:
    print(FA(i))

