sandy_age_premise = 4
molly_age_premise = 3
sandy_age_hypothesis = 5
molly_age_hypothesis = 3

# the hypothesis refers to the ratio of the ages of Sandy and Molly mentioned in the premise
if sandy_age_hypothesis == sandy_age_premise and molly_age_hypothesis == molly_age_premise:
    # the hypothesis is consistent with the premise, so the label is neutral
    label = "neutral"
elif sandy_age_hypothesis > sandy_age_premise and molly_age_hypothesis > molly_age_premise:
    # the hypothesis contradicts the premise, as the ratios are different
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio, so any ratio consistent with the estimate is consistent with the premise
    label = "entailment"

print(label)
