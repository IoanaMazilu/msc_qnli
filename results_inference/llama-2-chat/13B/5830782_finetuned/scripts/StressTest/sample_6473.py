average_salary_premise = 4000
average_salary_hypothesis = 4000

# the hypothesis refers to the average salary of Raj, Roshan and Thomas mentioned in the premise
if average_salary_hypothesis <= average_salary_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives the exact average salary
    # any average salary greater than 'average_salary_premise' contradicts the premise
    label = "contradiction"

print(label)
