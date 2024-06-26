# Define variables for the numerical entities in the premise and hypothesis
monthly_salary_premise = 1200
monthly_salary_hypothesis = 3200

# Extract all quantities as valid numbers
monthly_salary_premise = float(monthly_salary_premise)
monthly_salary_hypothesis = float(monthly_salary_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if monthly_salary_hypothesis <= monthly_salary_premise:
    # Check if the estimate of'monthly_salary_hypothesis' contradicts the number of cookie sales in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
