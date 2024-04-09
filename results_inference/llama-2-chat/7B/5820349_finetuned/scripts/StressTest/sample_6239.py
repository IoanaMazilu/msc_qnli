socks_pairs_premise = 10
socks_pairs_hypothesis = 20

# the hypothesis refers to the number of sock pairs John has, which is also mentioned in the premise
if socks_pairs_hypothesis!= socks_pairs_premise:
    # check if the number of sock pairs in the hypothesis contradicts the number of sock pairs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
