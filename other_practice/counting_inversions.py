import math
import traceback

def counting_inversions(ip):
    return counting_inversions_rec(ip)

def counting_inversions_rec(input_list):
    """
    Recursive implementaton of merge sort
    :param input_list:
    :param start:
    :param end:
    :return:
    """
    try:

        if len(input_list) <= 1:
            return 0, input_list
        else:
            pivot = int(math.floor(len(input_list)/2))
            inversions, first_half = counting_inversions(input_list[:pivot])
            inv_t, second_half = counting_inversions(input_list[pivot:])
            inversions = inversions + inv_t
            inv_t, merged = merge(first_half, second_half)
            inversions = inversions + inv_t
        return inversions, merged
    except Exception as exc:
        traceback.print_exc()
        raise exc


def merge(list_1, list_2):
    """
    The MERGE step of merge sort
    :param list_1:
    :param list_2:
    :return: merged sorted list -> a combination of list_1 and list_2
    """
    try:
        i = 0
        j = 0
        m = 0
        merged_list = list()
        inver = 0
        while i < len(list_1) and j < len(list_2):
            if list_1[i] <= list_2[j]:
                merged_list.append(list_1[i])
                i = i+1
            else:
                merged_list.append(list_2[j])
                inver = inver + len(list_1[i:])
                j = j+1

        while i < len(list_1):
            merged_list.append(list_1[i])
            i = i+1
        while j < len(list_2):
            merged_list.append(list_2[j])
            j = j + 1
        return inver, merged_list
    except Exception as exc:
        raise exc

if __name__ == '__main__':
    ip = [5,2,6,1,0]
    print(counting_inversions(ip)[0])
