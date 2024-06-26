# Define variables for the premise and hypothesis
num_people_premise = 7
num_people_hypothesis = 6

# Check if the hypothesis value contradicts the premise
if num_people_hypothesis > num_people_premise:
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
