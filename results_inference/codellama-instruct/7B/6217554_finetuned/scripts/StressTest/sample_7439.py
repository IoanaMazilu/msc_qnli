fastest_horses_premise = 3
fastest_horses_hypothesis = 4

if fastest_horses_hypothesis!= fastest_horses_premise:
    # check if the number of fastest horses in the hypothesis contradicts the number of fastest horses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
