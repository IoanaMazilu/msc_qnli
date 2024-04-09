future_years_premise = 10
future_years_hypothesis = 80

# the hypothesis refers to the future years mentioned in the premise
if future_years_hypothesis < future_years_premise:
    # check if the number of future years in the hypothesis contradicts the number of future years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
