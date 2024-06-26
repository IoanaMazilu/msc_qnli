saving_decrease_premise = 30
saving_decrease_hypothesis = 80

# the hypothesis refers to the decrease in saving amount mentioned in the premise
if saving_decrease_hypothesis < saving_decrease_premise:
    # check if the percentage of decrease in saving amount in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
