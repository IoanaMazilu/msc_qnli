ratio_premise = 5/4
ratio_hypothesis = 5/4

if ratio_hypothesis >= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives a specific ratio for the ages of Sameer and Anand
    # any ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)
