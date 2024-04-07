# Premise: Bob is about to hang his 8 shirts in the wardrobe.
# Hypothesis: Bob is about to hang his less than 8 shirts in the wardrobe.
# Golden Label: contradiction

shirts_premise = 8
shirts_hypothesis = 8

# the hypothesis refers to the number of shirts Bob is about to hang in his wardrobe, which is also mentioned in the premise
if shirts_hypothesis >= shirts_premise:
    # check if the hypothesis value contradicts the estimate of 'less than shirts_hypothesis'
    label = "contradiction"
else:
    # the premise gives a specific number of shirts
    # any number of shirts less than 'shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

