average_salary_premise = 4000
average_salary_hypothesis = 4000

if average_salary_hypothesis <= average_salary_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_salary_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average salary
    # any number greater than 'average_salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
