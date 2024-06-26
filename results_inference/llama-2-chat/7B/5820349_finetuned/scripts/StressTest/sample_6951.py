arun_future_age_premise = 40
arun_future_years_premise = 5
arun_future_age_hypothesis = 40
arun_future_years_hypothesis = 2

# the hypothesis refers to Arun's future age and the number of years later, mentioned in the premise
if arun_future_age_premise!= arun_future_age_hypothesis:
    # check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
elif arun_future_years_hypothesis >= arun_future_years_premise:
    # check if the number of years later in the hypothesis contradicts the number of years later reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
