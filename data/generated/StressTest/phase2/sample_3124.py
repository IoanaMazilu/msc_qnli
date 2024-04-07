# Premise: He will be more than 4/3 times as old as Tom 6 years hence.
# Hypothesis: He will be 5/3 times as old as Tom 6 years hence.
# Golden Label: neutral

old_ratio_premise = 4/3
old_ratio_hypothesis = 5/3

# the hypothesis talks about the ratio of the ages of the two people referenced in the premise, 6 years hence
if old_ratio_hypothesis <= old_ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimate of more than 'old_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the ages
    # any ratio greater than 'old_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

