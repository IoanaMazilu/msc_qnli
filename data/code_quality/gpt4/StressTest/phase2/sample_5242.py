level1_employees_premise = 62
level1_employees_hypothesis = 72
graduates_premise = 20
graduates_hypothesis = 20

# the hypothesis refers to the number of level-1 employees and graduates mentioned in the premise
if level1_employees_hypothesis <= level1_employees_premise:
    # check if the number of 'level1_employees_hypothesis' contradicts the estimate of more than 'level1_employees_premise'
    label = "contradiction"
elif graduates_hypothesis != graduates_premise:
    # check if the number of graduates in the hypothesis contradicts the number of graduates reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of level-1 employees
    # any number of level-1 employees greater than 'level1_employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
