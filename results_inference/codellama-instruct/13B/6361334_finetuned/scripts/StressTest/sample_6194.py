salary_premise = 150
salary_hypothesis = 150

# the hypothesis refers to the salary mentioned in the premise
if salary_hypothesis >= salary_premise:
    # check if the estimate of'salary_hypothesis' contradicts the salary in the premise
    label = "contradiction"
else:
    # the premise gives an exact salary, but the hypothesis gives a lower bound
    # any salary greater than'salary_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
