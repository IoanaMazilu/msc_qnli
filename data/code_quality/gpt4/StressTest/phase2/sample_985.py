sock_pairs_premise = 72
sock_pairs_hypothesis = 12

# the hypothesis refers to the number of sock pairs Angela has, also mentioned in the premise
if sock_pairs_hypothesis >= sock_pairs_premise:
    # check if the hypothesis value contradicts the estimate of less than 'sock_pairs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the sock pairs
    # any number of sock pairs less than 'sock_pairs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
