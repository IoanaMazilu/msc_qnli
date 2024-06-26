saving_decrease_percentage_premise = 50
saving_decrease_percentage_hypothesis = 20

# the hypothesis refers to the decrease in savings mentioned in the premise
if saving_decrease_percentage_hypothesis >= saving_decrease_percentage_premise:
    # check if the estimate of 'saving_decrease_percentage_hypothesis' contradicts the decrease percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
