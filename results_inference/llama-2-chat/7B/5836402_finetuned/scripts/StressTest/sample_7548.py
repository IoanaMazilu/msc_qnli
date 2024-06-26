saving_decrease_premise = 30
saving_decrease_hypothesis = 80

# the hypothesis refers to the percentage of saving decrease due to loan payment mentioned in the premise
if saving_decrease_hypothesis >= saving_decrease_premise:
    # check if the estimate of'saving_decrease_hypothesis' contradicts the percentage of saving decrease in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
