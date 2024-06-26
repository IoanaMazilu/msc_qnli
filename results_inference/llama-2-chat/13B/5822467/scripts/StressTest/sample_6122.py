# Define variables with representative names for the numerical entities in both inputs
sanoop_returned_premise = 4
sanoop_returned_hypothesis = 8
average_price_remaining_premise = float(input("Enter the average price of the remaining t-shirts in the premise: "))
average_price_remaining_hypothesis = float(input("Enter the average price of the remaining t-shirts in the hypothesis: "))

# Extract all quantities as valid numbers (integers or floats)
sanoop_returned_premise = int(sanoop_returned_premise)
sanoop_returned_hypothesis = int(sanoop_returned_hypothesis)
average_price_remaining_premise = float(average_price_remaining_premise)
average_price_remaining_hypothesis = float(average_price_remaining_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments

# Compare the number of t-shirts returned in the premise and hypothesis
if sanoop_returned_hypothesis > sanoop_returned_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif sanoop_returned_hypothesis == sanoop_returned_premise:
    # Check if the hypothesis value is consistent with the premise value
    label = "neutral"
else:
    # Check if the premise value is a lower bound for the hypothesis value
    label = "entailment"

# Compare the average price of the remaining t-shirts in the premise and hypothesis
if average_price_remaining_hypothesis > average_price_remaining_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif average_price_remaining_hypothesis == average_price_remaining_premise:
    # Check if the hypothesis value is consistent with the premise value
    label = "neutral"
else:
    # Check if the premise value is a lower bound for the hypothesis value
    label = "entailment"

print(label)
