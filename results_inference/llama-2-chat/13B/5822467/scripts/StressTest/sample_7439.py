fastest_horses_premise = 3
fastest_horses_hypothesis = 4

# the hypothesis refers to the number of fastest horses to be submitted to the Kentucky Derby
if fastest_horses_hypothesis <= fastest_horses_premise:
    # check if the hypothesis value contradicts the estimate of 'fastest_horses_premise'
    label = "contradiction"
elif fastest_horses_premise!= fastest_horses_hypothesis:
    # check if the number of fastest horses in the hypothesis contradicts the number of fastest horses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
