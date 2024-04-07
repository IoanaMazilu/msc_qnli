# Premise: At present, the ratio between the ages of Arun and Deepak is more than 3:3.
# Hypothesis: At present, the ratio between the ages of Arun and Deepak is 4:3.
# Golden Label: neutral

ratio_premise = 3/3
ratio_hypothesis = 4/3

# the hypothesis refers to the same ratio between the ages of Arun and Deepak as mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

