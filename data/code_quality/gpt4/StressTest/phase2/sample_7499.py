jane_age_premise = 34
jane_age_hypothesis = 44
baby_sitting_stop_premise = 10
baby_sitting_stop_hypothesis = 10

# the hypothesis refers to Jane's age and when she stopped baby-sitting, both mentioned in the premise
if jane_age_hypothesis != jane_age_premise:
    # check if Jane's age in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif baby_sitting_stop_hypothesis != baby_sitting_stop_premise:
    # check if the time when Jane stopped baby-sitting in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
