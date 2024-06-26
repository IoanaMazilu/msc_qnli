total_ages_premise = 45
total_ages_hypothesis = 75

# the hypothesis refers to the total ages of Amar, Akbar and Anthony mentioned in the premise
if total_ages_premise!= total_ages_hypothesis:
    # check if the total ages in the hypothesis contradicts the total ages reported in the premise
    label = "contradiction"
else:
    # if the total ages in the hypothesis does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
