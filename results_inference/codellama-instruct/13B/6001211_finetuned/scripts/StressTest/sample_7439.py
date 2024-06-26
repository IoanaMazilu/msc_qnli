horses_premise = 25
horses_hypothesis = 25
fastest_horses_premise = 3
fastest_horses_hypothesis = 4

# the hypothesis refers to the number of horses and the fastest horses mentioned in the premise
if horses_premise!= horses_hypothesis:
    # check if the number of horses in the hypothesis contradicts the number of horses reported in the premise
    label = "contradiction"
elif fastest_horses_premise!= fastest_horses_hypothesis:
    # check if the number of fastest horses in the hypothesis contradicts the number of fastest horses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)