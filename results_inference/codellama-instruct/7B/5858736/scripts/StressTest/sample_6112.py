# Define variables with representative names for the numerical entities in both inputs
num_level1_employees_premise = 60
num_college_grads_premise = 30
num_level1_employees_hypothesis = 80
num_college_grads_hypothesis = 30

# Extract all quantities as valid numbers (integers or floats)
num_level1_employees_premise = int(num_level1_employees_premise)
num_college_grads_premise = int(num_college_grads_premise)
num_level1_employees_hypothesis = int(num_level1_employees_hypothesis)
num_college_grads_hypothesis = int(num_college_grads_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if num_level1_employees_hypothesis <= num_level1_employees_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'num_level1_employees_premise'
    label = "contradiction"
elif num_college_grads_hypothesis!= num_college_grads_premise:
    # Check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
