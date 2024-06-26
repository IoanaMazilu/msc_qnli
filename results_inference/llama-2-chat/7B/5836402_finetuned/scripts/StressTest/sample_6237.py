socks_pair_premise = 10
socks_pair_hypothesis = 40

# the hypothesis refers to the number of pairs of socks John has, which is also mentioned in the premise
if socks_pair_hypothesis >= socks_pair_premise:
    # check if the estimate of'socks_pair_hypothesis' contradicts the number of pairs of socks in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
