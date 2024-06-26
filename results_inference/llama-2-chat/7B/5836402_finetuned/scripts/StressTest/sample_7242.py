father_age_premise = 2*Shankar_age_premise
father_age_hypothesis = 2*Shankar_age_hypothesis
future_years = 10

# the hypothesis refers to the future years, which are also mentioned in the premise
if future_years >= father_age_hypothesis:
    # check if the estimate of 'father_age_hypothesis' contradicts the number of future years in the premise
    label = "contradiction"
elif father_age_hypothesis > future_years:
    # check if the father's age in the hypothesis contradicts the number of future years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
