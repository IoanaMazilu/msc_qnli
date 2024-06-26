# Define variables with representative names for the numerical entities in both inputs
employees_level_1_premise = 80
employees_level_1_hypothesis = 10
college_graduates_premise = 30
college_graduates_hypothesis = 30

# Extract all quantities as valid numbers (integers or floats)
employees_level_1_premise = int(employees_level_1_premise)
employees_level_1_hypothesis = int(employees_level_1_hypothesis)
college_graduates_premise = int(college_graduates_premise)
college_graduates_hypothesis = int(college_graduates_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if employees_level_1_hypothesis <= employees_level_1_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'employees_level_1_premise'
    label = "contradiction"
elif college_graduates_hypothesis!= college_graduates_premise:
    # Check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
