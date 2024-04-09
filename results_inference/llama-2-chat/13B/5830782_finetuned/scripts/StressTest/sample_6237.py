socks_pairs_premise = 10
socks_pairs_hypothesis = 40

# the hypothesis refers to the number of socks pairs John has, which is also mentioned in the premise
if socks_pairs_premise >= socks_pairs_hypothesis:
    # check if the number of socks pairs in the premise contradicts the hypothesis estimate of less than'socks_pairs_hypothesis'
    label = "contradiction"
elif socks_pairs_premise == socks_pairs_hypothesis:
    # check if the number of socks pairs in the premise contradicts the hypothesis estimate of less than'socks_pairs_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
