salary_premise = 1200
salary_hypothesis = 3200

# the hypothesis refers to the monthly salary of Mary
if salary_hypothesis <= salary_premise:
    # check if the hypothesis value contradicts the estimate of $1200
    label = "contradiction"
else:
    # the premise gives only an estimate for the monthly salary of Mary
    # any amount less than $3200 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
