arun_age_future_premise = 40
arun_age_future_hypothesis = 40
years_future_premise = 5
years_future_hypothesis = 2

# the hypothesis refers to Arun's future age and the number of years mentioned in the premise
if arun_age_future_hypothesis!= arun_age_future_premise:
    # check if the future age of Arun in the hypothesis contradicts the future age of Arun in the premise
    label = "contradiction"
elif years_future_hypothesis >= years_future_premise:
    # check if the number of years in the future in the hypothesis contradicts the number of years in the future in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
