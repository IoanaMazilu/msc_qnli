average_increase_premise = 2
average_increase_hypothesis = 7

# the hypothesis refers to the desired average increase mentioned in the premise
if average_increase_hypothesis <= average_increase_premise:
    # check if the estimate of 'average_increase_hypothesis' contradicts the desired average increase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
