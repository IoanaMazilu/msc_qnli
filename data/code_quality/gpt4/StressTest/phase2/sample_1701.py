hunters_premise = 1500
hunters_hypothesis = 4500

# the hypothesis refers to the number of hunters in Piscataquis County mentioned in the premise
if hunters_hypothesis < hunters_premise:
    # check if the number of hunters in the hypothesis contradicts the number of hunters reported in the premise
    label = "contradiction"
elif hunters_hypothesis == hunters_premise:
    # if the number of hunters in the hypothesis exactly match the number in the premise, then we can infer entailment
    label = "entailment"
else:
    # the hypothesis gives an estimate (less than 'hunters_hypothesis') for the number of hunters
    # this is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
