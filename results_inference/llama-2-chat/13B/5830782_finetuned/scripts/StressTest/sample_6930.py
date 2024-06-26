sandy_future_age_premise = 30
sandy_future_years_premise = 6
sandy_future_age_hypothesis = 30
sandy_future_years_hypothesis = 2

# the hypothesis refers to the future age and the number of years in the future when Sandy will be 30 years old
if sandy_future_age_premise!= sandy_future_age_hypothesis:
    # check if the future age in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
elif sandy_future_years_premise <= sandy_future_years_hypothesis:
    # check if the number of future years in the hypothesis contradicts the number of future years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
