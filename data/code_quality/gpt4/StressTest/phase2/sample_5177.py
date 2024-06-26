cathy_stretch_premise = 24
cathy_stretch_hypothesis = 24

# the hypothesis refers to the time Cathy needs to stretch, mentioned also in the premise
if cathy_stretch_hypothesis > cathy_stretch_premise:
    # check if the time mentioned in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
elif cathy_stretch_hypothesis == cathy_stretch_premise:
    # if the times mentioned in both sentences are equal, we can infer entailment
    label = "entailment"
else:
    # if the time in the hypothesis is less than the time in the premise, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
