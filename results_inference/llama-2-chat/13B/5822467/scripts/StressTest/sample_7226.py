# Define variables with representative names for the numerical entities in both inputs
oa_premise = 2
ac_premise = 4
bd_premise = 6

# Extract all quantities as valid numbers (integers or floats)
oa_hypothesis = float(input("Enter the value of OA: "))
ac_hypothesis = float(input("Enter the value of AC: "))
bd_hypothesis = float(input("Enter the value of BD: "))

# Use brief comments to explain what comparison you do between the defined variables
# (do not use their values in the comments)

# Compare the values of OA and OB in the hypothesis with the values in the premise
if oa_hypothesis > oa_premise:
    # Check if the estimate of 'oa_hypothesis' contradicts the value of 'oa_premise'
    label = "contradiction"
elif ac_hypothesis == ac_premise and bd_hypothesis == bd_premise:
    # Check if the hypothesis values and estimates do not contradict the premise ones
    label = "entailment"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
