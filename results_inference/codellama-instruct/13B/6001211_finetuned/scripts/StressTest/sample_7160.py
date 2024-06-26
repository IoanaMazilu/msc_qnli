sandy_age_future_premise = 38
sandy_age_future_hypothesis = 38
years_future_premise = 6
years_future_hypothesis = 4

# the hypothesis refers to Sandy's future age and the number of years in the future mentioned in the premise
if sandy_age_future_hypothesis!= sandy_age_future_premise:
    # check if the future age of Sandy in the hypothesis contradicts the future age of Sandy in the premise
    label = "contradiction"
elif years_future_hypothesis > years_future_premise:
    # check if the number of years in the future in the hypothesis contradicts the number of years in the future in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
