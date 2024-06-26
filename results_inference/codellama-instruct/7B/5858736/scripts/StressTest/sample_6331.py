# Define variables for the numerical entities in the premise and hypothesis
num_boxes_premise = 8
num_cases_hypothesis = 5
num_hours_hypothesis = 2

# Extract all quantities as valid numbers
num_boxes_premise = int(num_boxes_premise)
num_cases_hypothesis = int(num_cases_hypothesis)
num_hours_hypothesis = int(num_hours_hypothesis)

# Perform calculations
num_cases_premise = num_boxes_premise / num_cases_hypothesis
num_cases_premise = int(num_cases_premise)

# Check if the hypothesis value contradicts the premise
if num_cases_premise <= num_cases_hypothesis:
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
