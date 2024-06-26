saving_decrease_premise = 10
saving_decrease_hypothesis = 60

# the hypothesis refers to the percentage of saving decrease due to loan payment mentioned in the premise
if saving_decrease_hypothesis <= saving_decrease_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
