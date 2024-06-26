years_future_premise = 10
years_future_hypothesis = 80

# the hypothesis refers to the same situation as the premise but with a different time frame
if years_future_hypothesis < years_future_premise:
    # check if the time frame in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
else:
    # if the time frame in the hypothesis does not contradict the time frame in the premise, we can infer entailment
    label = "entailment"

print(label)
