# Premise: Listco employs 72 level-1 employees, 20 of whom are college graduates.
# Hypothesis: Listco employs more than 72 level-1 employees, 20 of whom are college graduates.
# Golden Label: contradiction

level1_employees_premise = 72
level1_employees_hypothesis = 72
college_graduates_premise = 20
college_graduates_hypothesis = 20

# the hypothesis refers to the number of level-1 employees and the number of college graduates mentioned in the premise
if level1_employees_hypothesis != level1_employees_premise:
    # check if the number of level-1 employees in the hypothesis contradicts the number of level-1 employees reported in the premise
    label = "contradiction"
elif college_graduates_hypothesis != college_graduates_premise:
    # check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

