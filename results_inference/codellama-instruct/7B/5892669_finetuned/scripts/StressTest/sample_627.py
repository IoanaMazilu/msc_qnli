socks_premise = 10
socks_hypothesis = 70

# the hypothesis refers to the number of pairs of matched socks John has, which is also mentioned in the premise
if socks_premise >= socks_hypothesis:
    # check if the number of pairs of socks in the premise contradicts the estimate of less than'socks_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
