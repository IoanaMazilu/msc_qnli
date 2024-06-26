age_premise = 82
age_hypothesis = 32
baby_sitting_years_premise = 12
baby_sitting_years_hypothesis = 12

# the hypothesis refers to the age of Jane and the number of years she stopped baby-sitting, both mentioned in the premise
if age_premise <= age_hypothesis:
    # check if the estimate of 'age_hypothesis' contradicts the age in the premise
    label = "contradiction"
elif baby_sitting_years_hypothesis!= baby_sitting_years_premise:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
