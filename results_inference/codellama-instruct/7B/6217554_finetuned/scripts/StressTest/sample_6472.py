average_salary_premise = 5000
average_salary_hypothesis = 4000

if average_salary_hypothesis >= average_salary_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_salary_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average salary
    # any number of salary less than 'average_salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
