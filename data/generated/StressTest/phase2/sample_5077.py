# Premise: Right now, the ratio between the ages of Sandy and Molly is more than 1:3.
# Hypothesis: Right now, the ratio between the ages of Sandy and Molly is 4:3.
# Golden Label: neutral

age_ratio_premise = 1/3
age_ratio_hypothesis = 4/3

# the hypothesis talks about the ratio between the ages of Sandy and Molly, referenced also in the premise
if age_ratio_hypothesis <= age_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'age_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages 
    # any ratio greater than 'age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

