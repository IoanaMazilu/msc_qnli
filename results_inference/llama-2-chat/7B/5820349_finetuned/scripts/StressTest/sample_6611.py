years_future_premise = 18
years_future_hypothesis = 18

# the hypothesis refers to Molly's age in the future years mentioned in the premise
if years_future_hypothesis <= years_future_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
