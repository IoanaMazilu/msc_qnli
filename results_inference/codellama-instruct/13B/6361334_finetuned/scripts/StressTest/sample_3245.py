monthly_salary_premise = 0.6
monthly_salary_hypothesis = 0.5

# the hypothesis refers to the percentage of monthly salary spent on consumable items and clothes and transport
if monthly_salary_hypothesis >= monthly_salary_premise:
    # check if the hypothesis value contradicts the percentage of monthly salary spent on consumable items in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of monthly salary spent on consumable items
    # any percentage of monthly salary less than'monthly_salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
