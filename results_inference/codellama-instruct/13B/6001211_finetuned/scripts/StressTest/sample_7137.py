saving_decrease_premise = 10
saving_decrease_hypothesis = 60

# the hypothesis refers to the decrease in saving amount mentioned in the premise
if saving_decrease_hypothesis < saving_decrease_premise:
    # check if the estimate of'saving_decrease_hypothesis' contradicts the decrease in saving amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
