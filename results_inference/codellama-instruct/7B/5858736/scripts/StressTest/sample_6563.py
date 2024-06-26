# Define variables with representative names for the numerical entities in both inputs
test_score_premise = 0
test_score_hypothesis = 0
average_premise = 0
average_hypothesis = 0

# Extract all quantities as valid numbers (integers or floats)
test_score_premise = int(input("Enter the test score: "))
average_premise = int(input("Enter the average: "))

# Use brief comments to explain what comparison you do between the defined variables
if test_score_premise <= average_premise:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
elif test_score_hypothesis > average_hypothesis + 2:
    # Check if the hypothesis value is greater than the premise by more than 2 points
    label = "contradiction"
else:
    # If the hypothesis value is greater than the premise by less than 2 points, we can infer entailment
    label = "entailment"

print(label)
