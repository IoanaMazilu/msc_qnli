saving_decrease_premise = 30
saving_decrease_hypothesis = 80

# the hypothesis refers to the decrease in savings mentioned in the premise
if saving_decrease_hypothesis <= saving_decrease_premise:
    # check if the estimate of'saving_decrease_hypothesis' contradicts the decrease in savings in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)