fastest_horses_premise = 3
fastest_horses_hypothesis = 4
horses_premise = 25
horses_hypothesis = 25

# the hypothesis refers to the number of fastest horses to be submitted to the Kentucky Derby, as also mentioned in the premise
if fastest_horses_hypothesis <= fastest_horses_premise:
    # check if the hypothesis value contradicts the number of fastest horses in the premise
    label = "contradiction"
elif horses_hypothesis!= horses_premise:
    # check if the total number of horses in the hypothesis contradicts the total number of horses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
