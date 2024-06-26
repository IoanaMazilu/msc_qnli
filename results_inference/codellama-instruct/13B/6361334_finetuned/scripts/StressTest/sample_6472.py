salary_premise = 5000
salary_hypothesis = 4000

# the hypothesis refers to the average salary of Raj, Roshan and Thomas, which is also mentioned in the premise
if salary_hypothesis >= salary_premise:
    # check if the hypothesis value contradicts the estimate of less than'salary_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average salary
    # any average salary less than'salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
