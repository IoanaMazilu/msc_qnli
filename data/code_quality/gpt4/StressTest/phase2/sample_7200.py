pairs_of_socks_premise = 13
pairs_of_socks_hypothesis = 83

# the hypothesis refers to the number of matched socks pairs that Angela has, mentioned also in the premise
if pairs_of_socks_premise >= pairs_of_socks_hypothesis:
    # check if the number of socks pairs in the premise contradicts the estimate of less than 'pairs_of_socks_hypothesis'
    label = "contradiction"
elif pairs_of_socks_premise != pairs_of_socks_hypothesis:
    # the premise gives a specific number of pairs of socks
    # any number of pairs less than 'pairs_of_socks_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
