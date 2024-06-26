age_premise = 34
age_hypothesis = 44
stopped_babysitting_premise = 10

# the hypothesis refers to the age and the time when Jane stopped baby-sitting, both mentioned in the premise
if age_hypothesis <= age_premise:
    # check if the estimate of 'age_hypothesis' contradicts the age reported in the premise
    label = "contradiction"
elif stopped_babysitting_hypothesis!= stopped_babysitting_premise:
    # check if the time when Jane stopped baby-sitting in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
