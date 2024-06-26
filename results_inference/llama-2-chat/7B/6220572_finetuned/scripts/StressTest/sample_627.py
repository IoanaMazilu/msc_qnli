socks_pairs_premise = 10
socks_pairs_hypothesis = 70

# the hypothesis refers to the number of pairs of socks mentioned in the premise
if socks_pairs_hypothesis >= socks_pairs_premise:
    # check if the hypothesis value contradicts the number of pairs of socks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of socks
    # any number of pairs of socks greater than'socks_pairs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
