
# Ioannis Zisis, AM 2974

import csv

R_tsv_file = open("R_sorted.tsv", "r")
S_tsv_file = open("S_sorted.tsv", "r")
RintersectionS_file = open("RintersectionS.tsv", "w", newline='')
RintersectionS = csv.writer(RintersectionS_file, delimiter="\t")

r_line = R_tsv_file.readline().split()  # First line of R file.
s_line = S_tsv_file.readline().split()  # First line of S file.

while len(r_line) > 0:      # EOF check for R.
    while len(s_line) > 0:  # EOF check for S.

        s_previous = s_line

        if r_line[0] < s_line[0]:
            break                       # I use break everytime i want to read the next line in R.
        elif r_line[0] > s_line[0]:
            s_line = S_tsv_file.readline().split()

        if r_line[0] == s_line[0] and r_line[1] < s_line[1]:    # ex. R: (ab 30) and S: (ab 48)
            break
        elif r_line[0] == s_line[0] and r_line[1] > s_line[1]:  # ex. R: (bt 55) and S: (bt 52)
            s_line = S_tsv_file.readline().split()

        elif r_line[0] == s_line[0] and r_line[1] == s_line[1]:  # Only here i write the lines that are same in both files. (ex. bb 94)
            RintersectionS.writerow(s_line)
            s_line = S_tsv_file.readline().split()

        while s_previous[0] == s_line[0] and s_previous[1] == s_line[1]:    # To pass the duplicates in S.
            s_previous = s_line
            s_line = S_tsv_file.readline().split()

    r_previous = r_line
    r_line = R_tsv_file.readline().split()

    if len(r_line) > 0:
        while r_previous[0] == r_line[0] and r_previous[1] == r_line[1]:    # To pass the duplicates in R.
            r_previous = r_line
            r_line = R_tsv_file.readline().split()
