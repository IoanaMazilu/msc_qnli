# Premise: John has less than 30 pairs of matched socks.
# Hypothesis: John has 10 pairs of matched socks.
# Golden Label: neutral

pairs_socks_premise = 30
pairs_socks_hypothesis = 10

# the hypothesis refers to the number of pair of socks John has, which is also mentioned in the premise
if pairs_socks_hypothesis >= pairs_socks_premise:
    # check if the number of pair of socks in the hypothesis contradicts the statement of less than 'pairs_socks_premise' in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pair of socks
    # any number of pair of socks less than 'pairs_socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

