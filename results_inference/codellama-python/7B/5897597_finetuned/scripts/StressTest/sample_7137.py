decrease_percentage_premise = 10
decrease_percentage_hypothesis = 60

# the hypothesis refers to the decrease percentage of saving amount due to loan payment mentioned in the premise
if decrease_percentage_hypothesis < decrease_percentage_premise:
    # check if the estimate of 'decrease_percentage_hypothesis' contradicts the decrease percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
