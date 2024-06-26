socks_pairs_premise = 10
socks_pairs_hypothesis = 10

# the hypothesis refers to the number of sock pairs John has, which is also mentioned in the premise
if socks_pairs_hypothesis >= socks_pairs_premise:
    # check if the hypothesis estimate contradicts the number of sock pairs in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate doesn't contradict the premise, it must be entailed by it
    label = "entailment"

print(label)
