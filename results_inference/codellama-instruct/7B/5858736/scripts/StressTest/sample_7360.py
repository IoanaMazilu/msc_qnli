age_14_premise = 20
age_15_premise = 70
age_13_premise = 50
age_12_premise = 60
age_14_hypothesis = 80
age_15_hypothesis = 70
age_13_hypothesis = 50
age_12_hypothesis = 60

# check if the hypothesis values contradict the premise values
if age_14_hypothesis <= age_14_premise:
    label = "contradiction"
elif age_15_hypothesis <= age_15_premise:
    label = "contradiction"
elif age_13_hypothesis <= age_13_premise:
    label = "contradiction"
elif age_12_hypothesis <= age_12_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
