# Define variables for the premise and hypothesis
age_lewis_premise = 1
age_brown_premise = 2
age_lewis_hypothesis = 6
age_brown_hypothesis = 2

# Check if the ratio of the ages in the hypothesis is less than the ratio in the premise
if age_lewis_hypothesis / age_brown_hypothesis < age_lewis_premise / age_brown_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
