sock_pairs_premise = less_than_40
sock_pairs_hypothesis = 10

# the hypothesis refers to the number of sock pairs owned by John
if sock_pairs_hypothesis <= sock_pairs_premise:
    # check if the hypothesis value contradicts the estimate of less than 40 sock pairs in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of sock pairs
    # any number of sock pairs less than or equal to 10 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
