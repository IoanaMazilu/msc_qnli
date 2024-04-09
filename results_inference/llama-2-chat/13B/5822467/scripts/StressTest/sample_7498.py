age_premise = 54
age_hypothesis = 34
stop_babysitting_premise = 10
stop_babysitting_hypothesis = 10

# the hypothesis refers to Jane's age and the time she stopped baby-sitting
if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the estimate of Jane's current age in the premise
    label = "contradiction"
elif stop_babysitting_hypothesis!= stop_babysitting_premise:
    # check if the number of years since Jane stopped baby-sitting in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
