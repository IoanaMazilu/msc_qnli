# Premise: Jane is currently 34 years old, and she stopped baby-sitting 12 years ago.
# Hypothesis: Jane is currently more than 34 years old, and she stopped baby-sitting 12 years ago.
# Golden Label: contradiction

jane_age_premise = 34
jane_age_hypothesis = 34
babysitting_stop_premise = 12
babysitting_stop_hypothesis = 12

# the hypothesis refers to Jane's age and the number of years since she stopped babysitting
if jane_age_hypothesis != jane_age_premise:
    # check if the age in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif babysitting_stop_hypothesis != babysitting_stop_premise:
    # check if the number of years since Jane stopped babysitting in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

