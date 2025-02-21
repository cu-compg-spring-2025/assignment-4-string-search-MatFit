def get_shift_match_table(P):
    m = len(P)
    shift_match_table = {}

    for shift in range(m - 1, 0, -1): # Right to Left, backwards, by 1
        p_1 = m - 1
        p_2 = m - shift - 1

        while p_2 >= 0:
            if P[p_2] == P[p_1]:
                p_1 -= 1
                p_2 -= 1
                if p_2 < 0:
                    shift_match_table[shift] = m - shift
                    break
            else:
                shift_match_table[shift] = m - shift - p_2 - 1
                break
    shift_match_table[m] = 0
    return shift_match_table

def get_good_suffix_table(P):
    m = len(P)

    good_suffix_table = {}
    good_suffix_table[0] = 1

    shift_match_table = get_shift_match_table(P)

    for i in range(1, m + 1):
        good_suffix_table[i] = i + m

    for i in range(m, 0, -1):
        if shift_match_table[i] > 0:
            good_suffix_table[shift_match_table[i]] = i + shift_match_table[i]

    for i in range(m, 0, -1):
        if shift_match_table[i] + i == m:
            for j in range(shift_match_table[i] + 1, m+1):
                good_suffix_table[j] = min(good_suffix_table[j], j + i)

    return good_suffix_table

def get_bad_char_table(P):
    bad_char_table = {}
    #####################################################################
    ## ADD CODE HERE
    #####################################################################

    for i in range(len(P)):
        bad_char_table[P[i]] = i
    
    return bad_char_table
    

def boyer_moore_search(T, P):
    occurrences = []
    #####################################################################
    ## ADD CODE HERE
    #####################################################################

    P_len = len(P)
    T_len = len(T)
    if P_len == 0:
        return occurrences

    bad_char_table = get_bad_char_table(P)
    good_suffix_table = get_good_suffix_table(P)

    i = 0
    while i <= T_len - P_len:
        j = P_len - 1

        # Check if the pattern matches the text
        while j >= 0 and P[j] == T[i + j]:
            j -= 1

        # If the pattern matches the text
        if j < 0:
            occurrences.append(i)
            # When a full match is found, shift by the value given by the good suffix table,
            # but we can move forward at least one step.
            i += good_suffix_table[0] if good_suffix_table[0] > 0 else 1

        # If the pattern does not match the text
        else:
            # Get the shift value from the bad character table and the good suffix table, take the max. big shift big times
            shift_bc = j - bad_char_table.get(T[i + j], -1)
            shift_gs = good_suffix_table[j + 1]
            i += max(shift_bc, shift_gs, 1)


    return occurrences



