average_salary_premise = 4000
average_salary_hypothesis = 4000

# the hypothesis refers to the average salary of Raj, Roshan and Thomas mentioned in the premise
if average_salary_hypothesis <= average_salary_premise:
    # check if the estimate of 'average_salary_hypothesis' contradicts the average salary in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average salary
    # any average salary greater than 'average_salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
