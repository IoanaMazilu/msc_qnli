don_premise = 58
don_hypothesis = 18
mass_premise = 29
mass_hypothesis = 29
king_premise = None
king_hypothesis = None

# the hypothesis refers to the values of DON and MASS mentioned in the premise
if don_hypothesis >= don_premise and mass_hypothesis == mass_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
elif don_hypothesis < don_premise and mass_hypothesis == mass_premise:
    # check if the hypothesis values contradict the premise values
    label = "neutral"
else:
    # the premise gives only an estimate for the values of DON and MASS
    # any values of DON and MASS consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
