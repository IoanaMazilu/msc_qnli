average_salary_premise = 5000
average_salary_hypothesis = 4000

# the hypothesis refers to the average salary mentioned in the premise
if average_salary_hypothesis >= average_salary_premise:
    # check if the value of 'average_salary_hypothesis' contradicts the estimate of less than 'average_salary_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average salary
    # any value less than 'average_salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
