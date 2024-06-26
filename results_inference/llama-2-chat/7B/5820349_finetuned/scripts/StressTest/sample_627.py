socks_pairs_premise = 10
socks_pairs_hypothesis = 70

# the hypothesis refers to the number of sock pairs John has, which is also mentioned in the premise
if socks_pairs_premise >= socks_pairs_hypothesis:
    # check if the number of sock pairs in the premise contradicts the estimate of less than'socks_pairs_hypothesis'
    label = "contradiction"
else:
    # if the number of sock pairs in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
