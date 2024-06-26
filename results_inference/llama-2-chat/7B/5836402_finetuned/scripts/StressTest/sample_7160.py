future_age_premise = 38
future_age_hypothesis = 38
future_age_premise_years = 6
future_age_hypothesis_years = 4

# the hypothesis refers to the future age of Sandy mentioned in the premise
if future_age_hypothesis_years!= future_age_premise_years:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
elif future_age_hypothesis!= future_age_premise:
    # check if the future age in the hypothesis contradicts the future age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
