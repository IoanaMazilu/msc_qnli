years_future_premise = 6
years_future_hypothesis = 6
age_future_premise = 30
age_future_hypothesis = 30

# the hypothesis refers to the future age of Sandy mentioned in the premise
if years_future_hypothesis >= years_future_premise:
    # check if the hypothesis contradicts the premise's claim that Sandy will be 30 years old after 6 years
    label = "contradiction"
elif age_future_hypothesis!= age_future_premise:
    # check if the future age of Sandy in the hypothesis contradicts the future age of Sandy reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
