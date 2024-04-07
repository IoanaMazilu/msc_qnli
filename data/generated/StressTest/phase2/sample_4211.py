# Premise: He will be 5/3 times as old as Tom 6 years hence.
# Hypothesis: He will be less than 5/3 times as old as Tom 6 years hence.
# Golden Label: contradiction

ratio_premise = 5 / 3
ratio_hypothesis = 5 / 3

# the hypothesis refers to the same age ratio as in the premise but gives a different estimation
if ratio_hypothesis >= ratio_premise:
    # check if the hypothesis value contradicts the 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives a specific ratio for their ages
    # any ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

