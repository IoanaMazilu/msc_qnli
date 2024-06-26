years_future_premise = 21
years_future_hypothesis = 71

# the hypothesis refers to the same situation as the premise, but with a different time frame
if years_future_premise!= years_future_hypothesis:
    # check if the time frame in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
else:
    # if the time frames are the same, we can infer entailment
    label = "entailment"

print(label)
