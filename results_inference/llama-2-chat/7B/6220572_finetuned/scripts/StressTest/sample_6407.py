socks_pairs_premise = 15
socks_pairs_hypothesis = 75

# the hypothesis talks about the number of pairs of matched socks, referenced also in the premise
if socks_pairs_hypothesis <= socks_pairs_premise:
    # check if the hypothesis value contradicts the number of pairs of socks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of socks
    # any number of pairs of socks greater than'socks_pairs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
