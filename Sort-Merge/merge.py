#! python

#import common.py

def merge_sort(seq):
    if len(seq) <= 1: return seq

    L = len(seq)

    left_half = merge_sort(seq[0:L//2])
    right_half = merge_sort(seq[L//2:L])

    return merge_two_seq(left_half, right_half)

def merge_two_seq(seq1, seq2):
    i = j = 0
    seq = []
    while i < len(seq1) and j < len(seq2):
        if seq1[i] <= seq2[j]:
            seq.append(seq1[i]);
            i += 1
        else:
            seq.append(seq2[j]);
            j += 1

    if i < len(seq1): seq.extend(seq1[i:])
    if j < len(seq2): seq.extend(seq2[j:])

    return seq

arr = [9, 2, 14, 8, 5, 11, 4, 28, 73, 2]
arrSorted = merge_sort(arr)
print(arrSorted);

