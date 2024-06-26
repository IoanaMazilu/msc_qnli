arrested_premise = 6
arrested_hypothesis = 6

# the hypothesis mentions the number of protesters and counterprotesters arrested, which is also mentioned in the premise
if arrested_hypothesis!= arrested_premise:
    # check if the number of arrests in the hypothesis contradicts the number of arrests reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
