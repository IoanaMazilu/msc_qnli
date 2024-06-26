salary_premise = 1200
salary_hypothesis = 3200

# the hypothesis refers to the monthly salary mentioned in the premise
if salary_hypothesis <= salary_premise:
    # check if the estimate of'salary_hypothesis' contradicts the monthly salary in the premise
    label = "contradiction"
else:
    # the premise gives an exact value for the monthly salary
    # any value of monthly salary greater than'salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
