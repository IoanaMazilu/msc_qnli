years_back_premise = 6
years_back_hypothesis = 2

# the hypothesis refers to the same situation as the premise, but with a different time frame
if years_back_premise!= years_back_hypothesis:
    # check if the time frame in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
else:
    # if the time frames are the same, we can infer entailment
    label = "entailment"

print(label)
