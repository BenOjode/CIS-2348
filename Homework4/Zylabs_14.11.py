# ZyLabs 14.11
# Benjamin Ojode
# 1663352

def selection_sort_descend_trace(num_list):
    for i in range(len(num_list)):
        top_index = i
        for c in range(i + 1, len(num_list)):
            if num_list[c] > num_list[top_index]:
                top_index = c
        num_list[i], num_list[top_index] = num_list[top_index], num_list[i]
        if i != len(num_list) - 1:
            print(' '.join(str(x) for x in num_list), '')


def main():
    num_list = [int(x) for x in input().split()]
    selection_sort_descend_trace(num_list)


if __name__ == '__main__':
    main()