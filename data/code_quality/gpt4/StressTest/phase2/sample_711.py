saving_decrease_premise = 20
saving_decrease_hypothesis = 70

# the hypothesis refers to the decrease in John's bank savings mentioned in the premise
if saving_decrease_hypothesis < saving_decrease_premise:
    # check if the percentage of decrease in savings in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)