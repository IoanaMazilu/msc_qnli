age_premise = 32
age_hypothesis = 42
baby_sitting_premise = 10
baby_sitting_hypothesis = 10

# the hypothesis refers to the age of Jane and the number of years she stopped baby-sitting, both mentioned in the premise
if age_hypothesis >= age_premise:
    # check if the estimate of 'age_hypothesis' contradicts the age in the premise
    label = "contradiction"
elif baby_sitting_hypothesis!= baby_sitting_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)