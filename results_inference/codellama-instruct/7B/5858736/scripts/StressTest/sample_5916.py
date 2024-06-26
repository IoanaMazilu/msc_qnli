# Define variables with representative names for the numerical entities in both inputs
test_score_premise = 0
test_score_hypothesis = 0
average_premise = 0
average_hypothesis = 0

# Extract all quantities as valid numbers (integers or floats)
test_score_premise = int(input("Enter the test score for the premise: "))
test_score_hypothesis = int(input("Enter the test score for the hypothesis: "))
average_premise = int(input("Enter the average for the premise: "))
average_hypothesis = int(input("Enter the average for the hypothesis: "))

# Use brief comments to explain what comparison you do between the defined variables
if test_score_hypothesis <= test_score_premise:
    # Check if the hypothesis value contradicts the test score in the premise
    label = "contradiction"
elif average_hypothesis + 7 <= average_premise:
    # Check if the hypothesis value plus 7 contradicts the average in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
