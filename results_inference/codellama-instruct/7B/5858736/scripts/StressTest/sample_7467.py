# Define variables with representative names for the numerical entities in both inputs
college_graduates_premise = 10
college_graduates_hypothesis = 7

# Extract all quantities as valid numbers (integers or floats)
college_graduates_premise = float(college_graduates_premise)
college_graduates_hypothesis = float(college_graduates_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if college_graduates_hypothesis <= college_graduates_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'college_graduates_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of college graduates
    # Any number of college graduates greater than 'college_graduates_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
