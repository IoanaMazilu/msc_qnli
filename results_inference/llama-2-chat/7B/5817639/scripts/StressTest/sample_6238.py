less_than_40_pairs_premise = 40
matched_socks_hypothesis = 10

# the hypothesis refers to the number of pairs of matched socks, which is also mentioned in the premise
if matched_socks_hypothesis <= less_than_40_pairs_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_40_pairs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of matched socks
    # any number of pairs of matched socks greater than 'less_than_40_pairs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
