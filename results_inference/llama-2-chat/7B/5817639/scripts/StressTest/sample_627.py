socks_premise = 10
socks_hypothesis = 70

# the hypothesis talks about the number of pairs of matched socks, which is also mentioned in the premise
if socks_hypothesis <= socks_premise:
    # check if the hypothesis value contradicts the estimate of'socks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of matched socks
    # any number of pairs greater than'socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
