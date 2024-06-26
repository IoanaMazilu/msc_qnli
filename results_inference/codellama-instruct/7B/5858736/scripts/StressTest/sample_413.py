# Define variables for the premise and hypothesis
age_lewis_premise = 1
age_brown_premise = 2
age_lewis_hypothesis = 0.5
age_brown_hypothesis = 1

# Check if the hypothesis values contradict the premise
if age_lewis_hypothesis / age_brown_hypothesis > age_lewis_premise / age_brown_premise:
    label = "contradiction"
else:
    # The hypothesis values do not contradict the premise, but cannot be fully and explicitly entailed from the premise either
    label = "neutral"

print(label)
