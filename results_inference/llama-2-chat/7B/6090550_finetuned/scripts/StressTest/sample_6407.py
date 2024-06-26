y = 75
pairs_premise = 15

# the hypothesis talks about the number of pairs of matched socks Angela has, referenced also in the premise
if pairs_premise!= y:
    # check if the number of pairs in the hypothesis contradicts the number of pairs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
