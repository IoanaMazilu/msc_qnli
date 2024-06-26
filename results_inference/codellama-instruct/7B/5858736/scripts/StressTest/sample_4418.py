# Define variables with representative names for the numerical entities in both inputs
test_score_premise = 0
test_score_hypothesis = 0
average_premise = 0
average_hypothesis = 0

# Extract all quantities as valid numbers (integers or floats)
test_score_premise = int(input("Enter the test score for the premise: "))
average_premise = int(input("Enter the average for the premise: "))
test_score_hypothesis = int(input("Enter the test score for the hypothesis: "))
average_hypothesis = int(input("Enter the average for the hypothesis: "))

# Use brief comments to explain what comparison you do between the defined variables
if test_score_hypothesis <= test_score_premise:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
elif average_hypothesis - average_premise!= 3:
    # Check if the difference between the hypothesis and premise averages is not equal to 3
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
