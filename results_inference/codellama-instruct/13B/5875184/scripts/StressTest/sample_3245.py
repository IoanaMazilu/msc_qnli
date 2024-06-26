monthly_salary_premise = 60
monthly_salary_hypothesis = 50

# the hypothesis talks about the percentage of monthly salary spent on consumable items and clothes
if monthly_salary_hypothesis <= monthly_salary_premise:
    # check if the hypothesis value contradicts the estimate of more than'monthly_salary_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of monthly salary spent on consumable items
    # any percentage of monthly salary greater than'monthly_salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
