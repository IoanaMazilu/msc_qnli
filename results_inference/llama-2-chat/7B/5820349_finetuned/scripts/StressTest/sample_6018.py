jane_age_premise = 32
jane_age_hypothesis = 42
baby_sitting_stop_premise = 10
baby_sitting_stop_hypothesis = 10

# the hypothesis refers to Jane's age and the time when she stopped baby-sitting, both mentioned in the premise
if jane_age_premise >= jane_age_hypothesis:
    # check if the estimate of 'jane_age_hypothesis' contradicts Jane's age in the premise
    label = "contradiction"
elif baby_sitting_stop_hypothesis!= baby_sitting_stop_premise:
    # check if the time when Jane stopped baby-sitting in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
