# Define variables with representative names for the numerical entities in both inputs
level_1_employees_premise = 72
college_graduates_premise = 30
level_1_employees_hypothesis = 52
college_graduates_hypothesis = 30

# Extract all quantities as valid numbers (integers or floats)
level_1_employees_premise = int(level_1_employees_premise)
college_graduates_premise = int(college_graduates_premise)
level_1_employees_hypothesis = int(level_1_employees_hypothesis)
college_graduates_hypothesis = int(college_graduates_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if level_1_employees_hypothesis <= level_1_employees_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'level_1_employees_premise'
    label = "contradiction"
elif college_graduates_hypothesis!= college_graduates_premise:
    # Check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
