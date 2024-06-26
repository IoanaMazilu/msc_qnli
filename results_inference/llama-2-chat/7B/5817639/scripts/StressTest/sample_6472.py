average_salary_premise = 5000
average_salary_hypothesis = 4000

# the hypothesis talks about the average salary of a specific group of people, referenced also in the premise
if average_salary_hypothesis <= average_salary_premise:
    # check if the hypothesis value contradicts the estimate of the average salary in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average salary
    # any average salary greater than 'average_salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
