salary_premise = 3200
salary_hypothesis = 1200

# the hypothesis refers to the monthly salary mentioned in the premise
if salary_hypothesis >= salary_premise:
    # check if the hypothesis value contradicts the estimate of 'less than salary_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the monthly salary
    # any salary less than'salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
