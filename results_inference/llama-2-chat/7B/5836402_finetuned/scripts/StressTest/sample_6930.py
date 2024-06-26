future_age_premise = 30
future_age_hypothesis = 30
future_age_years_hypothesis = 2

# the hypothesis refers to Sandy's age in the future, which is also mentioned in the premise
if future_age_hypothesis <= future_age_premise:
    # check if the hypothesis value contradicts the estimate of more than 'future_age_premise' years
    label = "contradiction"
elif future_age_years_hypothesis!= future_age_premise:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
