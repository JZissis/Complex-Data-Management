
# Ioannis Zisis, AM 2974

import csv

R_tsv_file = open("R.tsv", "r")
RgroupbyS_file = open("RgroupbyS.tsv", "w", newline="")
RgroupbyS = csv.writer(RgroupbyS_file, delimiter="\t")



def sort_merge(array):
    if len(array) > 1:

        center = len(array)//2

        left_cut = array[:center]
        right_cut = array[center:]
        sort_merge(left_cut)            # Recursive implementation of sort merge algorithm.
        sort_merge(right_cut)
        merge(array, left_cut, right_cut)


def merge(array, left, right):

    if len(array) > len(left + right):              # To avoid creating duplicates and sorting problems, array always needs to have the same length with the sum of its left and right cut lengths.
        del array[-(len(array)-len(left+right)):]

    left_i = right_i = final_i = eq_joined = 0
    
    while left_i < len(left) and right_i < len(right):      # Main sorting loop.

        if left[left_i][0] == right[right_i][0]:            # In case of duplicates, add their number columns and insert them into the array.
            right[right_i][1] = str(int(left[left_i][1]) + int(right[right_i][1]))
            array[final_i] = right[right_i]
            left_i += 1
            right_i += 1
            eq_joined += 1          # This variable keeps count of the additions that happen and is equal to te reduction of the array's length.

        elif left[left_i][0] > right[right_i][0]:
            array[final_i] = right[right_i]
            right_i += 1

        else:
            array[final_i] = left[left_i]
            left_i += 1

        final_i += 1

    if eq_joined > 0:           # As explained in above comment, array length is decreased by eq_joined.
        del array[-eq_joined:]

    while left_i < len(left):           # Fill remaining elements in array.
        array[final_i] = left[left_i]
        final_i += 1
        left_i += 1


    while right_i < len(right):         # Fill remaining elements in array.
        array[final_i] = right[right_i]
        final_i += 1
        right_i += 1


arrayR = []

for row in R_tsv_file:          # Read the file.
    arrayR.append(row.split())

print('Starting grouping of contents...')
sort_merge(arrayR)
RgroupbyS.writerows(arrayR)
print('Completed and contents written in file.')

R_tsv_file.close()
RgroupbyS_file.close()