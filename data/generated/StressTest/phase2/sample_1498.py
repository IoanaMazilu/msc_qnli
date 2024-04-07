# Premise: Listco employs more than 30 level-1 employees, 30 of whom are college graduates.
# Hypothesis: Listco employs 60 level-1 employees, 30 of whom are college graduates.
# Golden Label: neutral

level1_employees_premise = 30
level1_employees_hypothesis = 60
graduates_premise = 30
graduates_hypothesis = 30

# the hypothesis refers to the number of level-1 employees and graduates mentioned in the premise
if level1_employees_hypothesis <= level1_employees_premise:
    # check if the number of 'level1_employees_hypothesis' contradicts the estimate of more than 'level1_employees_premise'
    label = "contradiction"
elif graduates_hypothesis != graduates_premise:
    # check if the number of graduates in the hypothesis contradicts the number of graduates reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of level-1 employees
    # the exact number of level-1 employees in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

