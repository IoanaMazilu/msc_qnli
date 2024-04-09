arun_future_age_premise = 26
arun_future_years_premise = 6
arun_future_age_hypothesis = 26
arun_future_years_hypothesis = 3

# the hypothesis refers to the future age and years of Arun mentioned in the premise
if arun_future_age_hypothesis!= arun_future_age_premise:
    # check if the future age in the hypothesis contradicts the future age in the premise
    label = "contradiction"
elif arun_future_years_hypothesis!= arun_future_years_premise:
    # check if the number of years in the future in the hypothesis contradicts the number of years in the future in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
