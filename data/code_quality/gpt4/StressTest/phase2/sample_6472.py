average_salary_premise = 5000
average_salary_hypothesis = 4000

# the hypothesis talks about the average salary of Raj, Roshan and Thomas, which is also mentioned in the premise
if average_salary_hypothesis >= average_salary_premise:
    # check if the hypothesis value contradicts the premise of less than 'average_salary_premise'
    label = "contradiction"
elif average_salary_hypothesis < average_salary_premise:
    # if the hypothesis value is less than the 'average_salary_premise', it can be explicitly entailed from the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the average salary
    # any average salary less than 'average_salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
