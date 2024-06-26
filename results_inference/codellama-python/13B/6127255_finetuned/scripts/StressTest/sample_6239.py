socks_premise = 10
socks_hypothesis = 20

# the hypothesis refers to the number of pairs of matched socks John has, which is also mentioned in the premise
if socks_hypothesis!= socks_premise:
    # check if the number of pairs of socks in the hypothesis contradicts the number of pairs of socks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
