
# Ioannis Zisis, AM 2974

import csv
import heapq as heap

R_tsv_file = open("R_sorted.tsv", "r")
S_tsv_file = open("S_sorted.tsv", "r")
RjoinS_file = open("RjoinS.tsv", "w", newline='')
RjoinS = csv.writer(RjoinS_file, delimiter="\t")

join_buffer = []
heap.heapify(join_buffer)  # Create the buffer using the heapq module.

key_j = S_tsv_file.readline().split()  # First line of S_sorted file.
key_i = R_tsv_file.readline().split()  # First line of R_sorted file.
maxsize = 0
count = 0

while len(key_i) > 0:                           # EOF check for R file.

    if len(key_j) > 0:                          # EOF check for S file.

        while key_i[0] == key_j[0]:
            item = key_i + [item for item in key_j if item != key_i[0]]
            RjoinS.writerow(item)
            heap.heappush(join_buffer, key_j)
            count+=1

            key_j = S_tsv_file.readline().split()       # Next line in S.

    previous_key_i = key_i
    key_i = R_tsv_file.readline().split()               # Next line in R.

    if len(join_buffer) > maxsize:
        maxsize = len(join_buffer)

    if len(key_i) > 0:                          # Range check for key_i.

        while key_i[0] == previous_key_i[0]:

            for k in range(len(join_buffer)):                # Here i copy the matched lines of the same alpharithmetic values.
                copy_item = key_i + [item for item in join_buffer[k] if item != key_i[0]]
                RjoinS.writerow(copy_item)
                count+=1

            previous_key_i = key_i
            key_i = R_tsv_file.readline().split()

        while len(join_buffer) > 0:    # No more matched lines,so i clear the buffer.
            heap.heappop(join_buffer)

        while key_i[0] > key_j[0]:              # In case R doesn't have a key which S has.
            key_j = S_tsv_file.readline().split()



print('Max size of buffer is:', maxsize)
print('Total elements in the output file:', count)

R_tsv_file.close()
S_tsv_file.close()
RjoinS_file.close()

