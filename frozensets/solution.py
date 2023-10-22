def find_common_elements(list1, list2):
    overlap = []
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    idx1 = 0
    idx2 = 0
    while idx1 < len(sorted_list1) and idx2 < len(sorted_list2):
        if sorted_list1[idx1] == sorted_list2[idx2]:
            overlap.append(sorted_list1[idx1])
            idx1 += 1
            idx2 += 1
        elif sorted_list1[idx1] < sorted_list2[idx2]:
            idx1 += 1
        else:
            idx2 += 1
    return frozenset(overlap)


