arun_future_age_premise = 26
arun_future_years_premise = 6
arun_future_age_hypothesis = 26
arun_future_years_hypothesis = 3

# the hypothesis refers to Arun's future age and the number of years until that age, mentioned in the premise
if arun_future_age_premise!= arun_future_age_hypothesis:
    # check if the future age in the hypothesis contradicts the future age mentioned in the premise
    label = "contradiction"
elif arun_future_years_hypothesis!= arun_future_years_premise:
    # check if the number of years until the future age in the hypothesis contradicts the number of years mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
