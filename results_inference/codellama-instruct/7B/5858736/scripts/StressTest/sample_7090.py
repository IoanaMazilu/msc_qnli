# Define variables with representative names for the numerical entities in both inputs
monthly_salary_premise = 3200
monthly_salary_hypothesis = 1200

# Extract all quantities as valid numbers (integers or floats)

# Check if the hypothesis value contradicts the estimate of less than'monthly_salary_premise'
if monthly_salary_hypothesis >= monthly_salary_premise:
    label = "contradiction"
else:
    # Any number of salary greater than'monthly_salary_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
