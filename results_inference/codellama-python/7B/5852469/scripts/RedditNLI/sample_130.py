salary_premise = 100000
salary_hypothesis = 100000

# the hypothesis and premise mention the same salary
if salary_hypothesis!= salary_premise:
    # check if the salary in the hypothesis contradicts the salary in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the salary
    # any estimate of the salary in the hypothesis greater or equal to'salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
