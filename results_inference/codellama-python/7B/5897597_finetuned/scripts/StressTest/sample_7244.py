years_future_premise = 10
years_future_hypothesis = 30

# the hypothesis refers to the same situation as the premise, but with a different number of years in the future
if years_future_hypothesis!= years_future_premise:
    # check if the number of years in the future in the hypothesis contradicts the number of years in the future in the premise
    label = "contradiction"
else:
    # if the number of years in the future in the hypothesis does not contradict the number of years in the future in the premise, we can infer entailment
    label = "entailment"

print(label)
