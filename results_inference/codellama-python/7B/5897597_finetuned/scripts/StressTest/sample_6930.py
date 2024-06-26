years_future_premise = 6
age_future_premise = 30
years_future_hypothesis = 2
age_future_hypothesis = 30

# the hypothesis refers to the future age of Sandy and the number of years mentioned in the premise
if years_future_hypothesis >= years_future_premise:
    # check if the hypothesis value contradicts the number of years in the premise
    label = "contradiction"
elif age_future_hypothesis!= age_future_premise:
    # check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
