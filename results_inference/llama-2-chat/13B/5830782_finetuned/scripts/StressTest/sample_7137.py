saving_decrease_premise = 10
saving_decrease_hypothesis = 60

# the hypothesis refers to the decrease in savings mentioned in the premise
if saving_decrease_hypothesis < saving_decrease_premise:
    # check if the hypothesis estimate contradicts the decrease in savings reported in the premise
    label = "contradiction"
elif saving_decrease_hypothesis > saving_decrease_premise:
    # check if the hypothesis estimate is greater than the decrease in savings reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
