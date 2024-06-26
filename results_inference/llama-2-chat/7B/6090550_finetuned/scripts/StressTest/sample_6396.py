y_premise = 1/3
y_hypothesis = 1/3

# the hypothesis refers to the percentage of airline passengers using Kennedy Airport, which is also mentioned in the premise
if y_hypothesis!= y_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
