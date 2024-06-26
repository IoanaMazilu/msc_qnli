socks_premise = 15
socks_hypothesis = 75

# the hypothesis refers to the number of pairs of matched socks Angela has, as mentioned in the premise
if socks_hypothesis!= socks_premise:
    # check if the number of pairs of socks in the hypothesis contradicts the number of pairs of socks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
