# Define variables for the premise and hypothesis
england_premise = 6
france_premise = 6
italy_premise = 0
england_hypothesis = 3
france_hypothesis = 11
italy_hypothesis = 0

# Check if the hypothesis contradicts the premise
if england_hypothesis > england_premise:
    label = "contradiction"
elif italy_hypothesis > italy_premise:
    label = "contradiction"
else:
    # The hypothesis does not contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
