# Define variables with representative names for the numerical entities in both inputs
employees_l1_premise = 80
employees_l1_hypothesis = 60
college_grads_l1_premise = 30
college_grads_l1_hypothesis = 30

# Extract all quantities as valid numbers (integers or floats)
employees_l1_premise = int(employees_l1_premise)
employees_l1_hypothesis = int(employees_l1_hypothesis)
college_grads_l1_premise = int(college_grads_l1_premise)
college_grads_l1_hypothesis = int(college_grads_l1_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if employees_l1_hypothesis <= employees_l1_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'employees_l1_premise'
    label = "contradiction"
elif college_grads_l1_hypothesis!= college_grads_l1_premise:
    # Check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
