monthly_salary_premise = 1200
monthly_salary_hypothesis = 3200

# the hypothesis talks about a higher monthly salary than the premise
if monthly_salary_hypothesis >= monthly_salary_premise:
    # check if the hypothesis value contradicts the estimate of the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the monthly salary
    # any higher monthly salary than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
