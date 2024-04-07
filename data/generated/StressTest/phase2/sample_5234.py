# Premise: 2000, Deepak's share is :
# Hypothesis: more than 2000, Deepak's share is :
# Golden Label: contradiction

deepak_share_premise = 2000
deepak_share_hypothesis = 2000

# the hypothesis refers to Deepak's share, which is also mentioned in the premise
if deepak_share_hypothesis > deepak_share_premise:
    # check if the hypothesis value contradicts the exact amount of 'deepak_share_premise'
    label = "contradiction"
else:
    # the premise gives an exact amount for Deepak's share
    # any amount equal to or less than 'deepak_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

