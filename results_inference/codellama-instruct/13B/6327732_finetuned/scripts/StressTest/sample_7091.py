monthly_salary_premise = 1200
monthly_salary_hypothesis = 3200

# the hypothesis refers to the monthly salary mentioned in the premise
if monthly_salary_hypothesis <= monthly_salary_premise:
    # check if the estimate of'monthly_salary_hypothesis' contradicts the monthly salary in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the monthly salary
    # any monthly salary greater than'monthly_salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
