arun_age_future_premise = 26
arun_age_future_hypothesis = 26
years_until_future_premise = 6
years_until_future_hypothesis = 3

# the hypothesis refers to the same future age of Arun as the premise, but at a different time
if arun_age_future_hypothesis!= arun_age_future_premise:
    # check if the future age of Arun in the hypothesis contradicts the future age of Arun in the premise
    label = "contradiction"
elif years_until_future_hypothesis!= years_until_future_premise:
    # check if the number of years until the future age of Arun in the hypothesis contradicts the number of years until the future age of Arun in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
