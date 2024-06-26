saving_decrease_premise = 30
saving_decrease_hypothesis = 20

# the hypothesis refers to the decrease in savings mentioned in the premise
if saving_decrease_hypothesis!= saving_decrease_premise:
    # check if the decrease in savings in the hypothesis contradicts the decrease in savings reported in the premise
    label = "contradiction"
else:
    # if the decrease in savings in the hypothesis does not contradict the decrease in savings reported in the premise, we can infer entailment
    label = "entailment"

print(label)
