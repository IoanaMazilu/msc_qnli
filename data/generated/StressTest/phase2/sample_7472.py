# Premise: Listco employs 72 level-1 employees, 30 of whom are college graduates.
# Hypothesis: Listco employs 62 level-1 employees, 30 of whom are college graduates.
# Golden Label: contradiction

level1_employees_premise = 72
level1_employees_hypothesis = 62
college_graduates_premise = 30
college_graduates_hypothesis = 30

# the hypothesis refers to the number of level-1 employees and college graduates at Listco mentioned in the premise
if level1_employees_premise != level1_employees_hypothesis:
    # check if the number of level-1 employees in the hypothesis contradicts the number of level-1 employees reported in the premise
    label = "contradiction"
elif college_graduates_premise != college_graduates_hypothesis:
    # check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

