percentage_premise = 1.0
value_hypothesis = 6 # in billion dollars

# the hypothesis and premise mention the change in net foreign assets of the Saudi central bank in March
if value_hypothesis > 0:
    # check if the value in the hypothesis contradicts the premise which states that the assets shrunk
    label = "contradiction"
elif percentage_premise!= 1.0:
    # check if the percentage in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # the premise gives only the percentage of shrinkage, not the absolute value
    # any value in the hypothesis that represents a shrinkage is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
