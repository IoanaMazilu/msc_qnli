years_future_premise = 10
years_future_hypothesis = 80

# the hypothesis refers to the same situation as the premise but with a different future time
if years_future_hypothesis < years_future_premise:
    # check if the future time in the hypothesis contradicts the future time in the premise
    label = "contradiction"
else:
    # if the future time in the hypothesis does not contradict the future time in the premise, we can infer entailment
    label = "entailment"

print(label)
