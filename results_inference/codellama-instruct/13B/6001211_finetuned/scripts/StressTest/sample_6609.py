years_future_premise = 18
years_future_hypothesis = 88

# the hypothesis refers to the time period referenced in the premise
if years_future_hypothesis < years_future_premise:
    # check if the time period in the hypothesis contradicts the time period in the premise
    label = "contradiction"
else:
    # if the time period in the hypothesis does not contradict the time period in the premise, we can infer entailment
    label = "entailment"

print(label)