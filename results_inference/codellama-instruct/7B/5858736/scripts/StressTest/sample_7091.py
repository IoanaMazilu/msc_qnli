# Define variables for the numerical entities in the premise and hypothesis
monthly_salary_premise = 1200
monthly_salary_hypothesis = 3200

# Check if the hypothesis value contradicts the premise
if monthly_salary_hypothesis <= monthly_salary_premise:
    # The hypothesis value contradicts the premise, so the hypothesis is a contradiction
    label = "contradiction"
else:
    # The hypothesis value does not contradict the premise, so the hypothesis is neutral
    label = "neutral"

print(label)
