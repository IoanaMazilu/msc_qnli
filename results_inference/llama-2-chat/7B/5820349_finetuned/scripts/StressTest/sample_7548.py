decrease_percentage_premise = 30
decrease_percentage_hypothesis = 80

# the hypothesis refers to the decrease percentage of John's bank savings mentioned in the premise
if decrease_percentage_premise >= decrease_percentage_hypothesis:
    # check if the estimate of 'decrease_percentage_hypothesis' contradicts the decrease percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
