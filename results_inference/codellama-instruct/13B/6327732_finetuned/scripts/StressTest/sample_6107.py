age_premise = 32
age_hypothesis = 32
baby_sitting_years_premise = 12
baby_sitting_years_hypothesis = 12

# the hypothesis refers to the age and the number of years since baby-sitting, both mentioned in the premise
if age_hypothesis <= age_premise:
    # check if the estimate of 'age_hypothesis' contradicts the age in the premise
    label = "contradiction"
elif baby_sitting_years_hypothesis!= baby_sitting_years_premise:
    # check if the number of years since baby-sitting in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
