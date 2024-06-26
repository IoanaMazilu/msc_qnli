# Define variables for the number of gangs in the premise and the hypothesis
gangs_premise = 8
gangs_hypothesis = 7

# Check if the hypothesis value contradicts the premise
if gangs_hypothesis > gangs_premise:
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
