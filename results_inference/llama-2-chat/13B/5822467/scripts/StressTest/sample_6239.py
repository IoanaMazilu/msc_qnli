sock_pairs_premise = 10
sock_pairs_hypothesis = 20

# the hypothesis talks about the number of sock pairs owned by John, referenced also in the premise
if sock_pairs_hypothesis <= sock_pairs_premise:
    # check if the hypothesis value contradicts the estimate of'sock_pairs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of sock pairs
    # any number of sock pairs greater than'sock_pairs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
