# Premise: Barbara has more than 1 shirts and 9 pants.
# Hypothesis: Barbara has 8 shirts and 9 pants.
# Golden Label: neutral

shirts_premise = 1
shirts_hypothesis = 8
pants_premise = 9
pants_hypothesis = 9

# the hypothesis refers to the number of Barbara's shirts and pants mentioned in the premise
if shirts_hypothesis <= shirts_premise:
    # check if the number of shirts in the hypothesis contradicts the estimate of more than 'shirts_premise'
    label = "contradiction"
elif pants_hypothesis != pants_premise:
    # check if the number of pants in the hypothesis contradicts the number of pants reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts
    # any number of shirts greater than 'shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

