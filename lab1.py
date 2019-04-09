def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    elif len(int_list) == 0:
        return None
    elif len(int_list) == 1:
        return int_list[0]
    else:
        maxint = int_list[0]
        for num in int_list:
            if num > maxint:
                maxint = num
        return maxint


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    elif len(int_list) == 0:
        return None
    elif len(int_list) == 1:
        return int_list
    else:
        return [int_list[len(int_list)-1]] + reverse_rec(int_list[:len(int_list)-1])



def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
    if int_list is None:
        raise ValueError
    elif len(int_list)==0:
        return None
    elif len(int_list) == 1 or low >= high:
        if int_list[0] == target:
            return 0
        else:
            return None
    else:
        mid = (low + high)//2
        if int_list[mid] == target:
            return mid
        elif int_list[low] == target:
            return low
        elif int_list[high] == target:
            return high
        else:
            if target < int_list[mid]:
                high = mid-1
            elif target > int_list[mid]:
                low = mid + 1
            return bin_search(target, low, high, int_list)

