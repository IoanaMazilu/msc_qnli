age_premise = 5
age_hypothesis = 85

# the hypothesis refers to Ariel Sharon's age, which is also mentioned in the premise
if age_hypothesis!= age_premise:
    # check if the age in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # if the age in the hypothesis matches the age in the premise, we can infer entailment
    label = "entailment"

print(label)
