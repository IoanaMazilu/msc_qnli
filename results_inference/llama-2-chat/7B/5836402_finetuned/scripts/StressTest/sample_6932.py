future_age_premise = 30
future_age_hypothesis = 30
future_years_hypothesis = 6
future_years_premise = 6

# the hypothesis refers to the future age of Sandy mentioned in the premise
if future_age_hypothesis >= future_age_premise:
    # check if the estimate of 'future_age_hypothesis' contradicts the future age in the premise
    label = "contradiction"
elif future_years_hypothesis!= future_years_premise:
    # check if the number of future years in the hypothesis contradicts the number of future years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
