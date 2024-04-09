average_salary_premise = 4000
average_salary_hypothesis = 5000

# the hypothesis talks about the average salary of Raj, Roshan and Thomas, which is also mentioned in the premise
if average_salary_hypothesis <= average_salary_premise:
    # check if the hypothesis value contradicts the estimate of the average salary in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average salary
    # any number less than the estimated average salary in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
