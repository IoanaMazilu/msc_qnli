# Define variables for the numerical entities in the premise and hypothesis
premise_salary = 5000
hypothesis_salary = 4000

# Extract all quantities as valid numbers
premise_salary = int(premise_salary)
hypothesis_salary = int(hypothesis_salary)

# Use brief comments to explain what comparison you do between the defined variables
if hypothesis_salary <= premise_salary:
    # Check if the estimate of 'hypothesis_salary' contradicts the number of salary mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
