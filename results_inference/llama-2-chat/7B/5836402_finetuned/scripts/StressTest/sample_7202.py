socks_premise = 13
socks_hypothesis = 83

# the hypothesis refers to the number of pairs of matched socks Angela has, which is also mentioned in the premise
if socks_premise!= socks_hypothesis:
    # check if the number of pairs of matched socks in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
