import math
import statistics

x = [1, 46, 23, 56, 123, 56, 125]

def matematika(x):
    print("Najmanjše število je:", min(x))
    print("Najvejčje število je:", max(x))
    povp = sum(x)/len(x)
    print("Povprečna vrednost je:", povp)
    y = min(x, key=lambda x:abs(x-povp))
    print("Vrednost najbližje povprečju je:", y)

matematika(x)
