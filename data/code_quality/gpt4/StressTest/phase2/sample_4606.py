years_back_premise = 8
years_back_hypothesis = 6

# the hypothesis refers to the same situation as the premise but with a different time
if years_back_hypothesis != years_back_premise:
    # the time difference in hypothesis contradicts the time difference in premise
    label = "contradiction"
else:
    # if the hypothesis time equals the premise time, we can infer entailment
    label = "entailment"

print(label)
