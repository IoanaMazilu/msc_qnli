years_future_premise = 5
years_future_hypothesis = 2
age_future_premise = 40
age_future_hypothesis = 40

# the hypothesis refers to the future age of Arun and the time until that age, mentioned in the premise
if years_future_hypothesis >= years_future_premise:
    # check if the estimate of 'years_future_hypothesis' contradicts the number of years until Arun's future age in the premise
    label = "contradiction"
elif age_future_hypothesis!= age_future_premise:
    # check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
