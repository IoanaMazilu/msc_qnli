mary_salary_premise = 3200
mary_salary_hypothesis = 1200

# the hypothesis refers to the monthly salary of Mary, which is also mentioned in the premise
if mary_salary_hypothesis >= mary_salary_premise:
    # check if the hypothesis value contradicts the estimate of less than'mary_salary_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the monthly salary
    # any monthly salary less than'mary_salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
