cleaning_time_premise = 3
cleaning_time_hypothesis = 3

# the hypothesis refers to the cleaning time at doubled speed of Anne mentioned in the premise
if cleaning_time_hypothesis <= cleaning_time_premise:
    # check if the cleaning time in hypothesis contradicts the cleaning time in premise
    label = "contradiction"
else:
    # if the cleaning time in hypothesis is more than the cleaning time in premise, we can infer entailment
    label = "entailment"

print(label)
