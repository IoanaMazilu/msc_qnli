age_premise = 32
age_hypothesis = 42
stop_babysitting_premise = 10

# the hypothesis refers to Jane's age and when she stopped baby-sitting
if age_hypothesis < age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif stop_babysitting_premise!= stop_babysitting_hypothesis:
    # check if the number of years since Jane stopped baby-sitting contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
