years_premise = 21
years_hypothesis = 71

# the hypothesis refers to the same situation as the premise but with a different time frame
if years_hypothesis!= years_premise:
    # check if the time frame in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
else:
    # if the time frames are the same, we can infer entailment
    label = "entailment"

print(label)
