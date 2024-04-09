# Define variables with representative names for the numerical entities in both inputs
jerry_avg_premise = 70  # premise: Jerry's current average is 70
jerry_avg_hypothesis = 72  # hypothesis: Jerry wants to raise his average by 2 points
fourth_test_score_premise = 60  # premise: If Jerry wants to raise his average by less than 7 points, what score must he earn on the fourth test?

# Extract all quantities as valid numbers (integers or floats)
jerry_avg_premise = int(jerry_avg_premise)
jerry_avg_hypothesis = int(jerry_avg_hypothesis)
fourth_test_score_premise = int(fourth_test_score_premise)

# Perform calculations if necessary
if jerry_avg_hypothesis > jerry_avg_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif fourth_test_score_premise < jerry_avg_hypothesis:
    # Check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # Check if the premise value and hypothesis value do not contradict each other
    label = "neutral"

print(label)
