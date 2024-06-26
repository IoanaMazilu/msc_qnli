years_premise = 21
years_hypothesis = 71

# the hypothesis refers to the same situation as the premise, but with different time frames
if years_premise!= years_hypothesis:
    # check if the time frames in the hypothesis contradict the time frames in the premise
    label = "contradiction"
else:
    # if the time frames in the hypothesis do not contradict the time frames in the premise, we can infer entailment
    label = "entailment"

print(label)
