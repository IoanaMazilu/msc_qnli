# Premise: 2000, Deepak's share is :
# Hypothesis: less than 2000, Deepak's share is :
# Golden Label: contradiction

share_deepak_premise = 2000
share_deepak_hypothesis = 2000

# the hypothesis refers to Deepak's share that is mentioned in the premise
if share_deepak_hypothesis >= share_deepak_premise:
    # check if the hypothesis value contradicts the premise value of 'share_deepak_premise'
    label = "contradiction"
else:
    # the premise states that Deepak's share is 'share_deepak_premise'
    # any share less than 'share_deepak_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

