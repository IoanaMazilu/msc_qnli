years_premise = 21
years_hypothesis = 71

# the hypothesis refers to the same situation as the premise, but with different time frames
if years_premise!= years_hypothesis:
    # check if the time frame in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
else:
    # if the time frames do not contradict, we can infer entailment
    label = "entailment"

print(label)
