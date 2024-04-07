# Premise: Listco employs 90 level-1 employees, 30 of whom are college graduates.
# Hypothesis: Listco employs more than 90 level-1 employees, 30 of whom are college graduates.
# Golden Label: contradiction

level1_employees_premise = 90
level1_employees_hypothesis = 90
college_graduates_employees_premise = 30
college_graduates_employees_hypothesis = 30

# the hypothesis refers to the number of level-1 employees and college graduate employees mentioned in the premise
if level1_employees_hypothesis != level1_employees_premise:
    # check if the number of level-1 employees in the hypothesis contradicts the number of level-1 employees reported in the premise
    label = "contradiction"
elif college_graduates_employees_hypothesis != college_graduates_employees_premise:
    # check if the number of college graduate employees in the hypothesis contradicts the number of college graduate employees reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

