sock_pairs_premise = 70
sock_pairs_hypothesis = 10

# the hypothesis refers to the number of pairs of socks owned by John
if sock_pairs_hypothesis <= sock_pairs_premise:
    # check if the estimate of'sock_pairs_hypothesis' contradicts the number of sock pairs in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of sock pairs
    # any number of sock pairs less than'sock_pairs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
