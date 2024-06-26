# Define variables for the numerical entities in the premise and hypothesis
scott_avg_premise = 88
scott_avg_hypothesis = 58

# Extract all quantities as valid numbers
scott_avg_premise = float(scott_avg_premise)
scott_avg_hypothesis = float(scott_avg_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if scott_avg_hypothesis >= scott_avg_premise:
    # Check if the hypothesis value contradicts the estimate of less than'scott_avg_premise'
    label = "contradiction"
else:
    # The hypothesis value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
