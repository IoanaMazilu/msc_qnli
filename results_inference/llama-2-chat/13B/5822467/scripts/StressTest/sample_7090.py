salary_premise = 3200
salary_hypothesis = 1200

# the hypothesis refers to Mary's monthly salary, mentioned in the premise
if salary_hypothesis <= salary_premise:
    # check if the hypothesis value contradicts the estimate of'salary_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Mary's monthly salary
    # any value of Mary's salary less than or equal to $1200 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
