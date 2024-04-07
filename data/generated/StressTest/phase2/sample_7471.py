# Premise: Listco employs more than 52 level-1 employees, 30 of whom are college graduates.
# Hypothesis: Listco employs 72 level-1 employees, 30 of whom are college graduates.
# Golden Label: neutral

level1_employees_premise = 52
level1_employees_hypothesis = 72
graduates_premise = 30
graduates_hypothesis = 30

# the hypothesis refers to the number of level-1 employees and graduates at Listco mentioned in the premise
if level1_employees_hypothesis <= level1_employees_premise:
    # check if the number of 'level1_employees_hypothesis' contradicts the number of level-1 employees in the premise
    label = "contradiction"
elif graduates_hypothesis != graduates_premise:
    # check if the number of graduates in the hypothesis contradicts the number of graduates reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of level-1 employees
    # any number of employees greater than 'level1_employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

