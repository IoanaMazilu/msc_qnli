total_age_premise = 56
total_age_hypothesis = 56

# the hypothesis refers to the total ages of Amar, Akbar and Anthony mentioned in the premise
if total_age_hypothesis != total_age_premise:
    # check if the total ages in the hypothesis contradicts the total ages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
