# Premise: Amtek employs 80 level-1 employees, 30 of whom are college graduates.
# Hypothesis: Amtek employs 10 level-1 employees, 30 of whom are college graduates.
# Golden Label: contradiction

level1_employees_premise = 80
level1_employees_hypothesis = 10
graduate_employees_premise = 30
graduate_employees_hypothesis = 30

# the hypothesis refers to the number of level-1 and college graduate employees mentioned in the premise
if level1_employees_hypothesis != level1_employees_premise:
    # check if the number of level-1 employees in the hypothesis contradicts the number of level-1 employees in the premise
    label = "contradiction"
elif graduate_employees_hypothesis > level1_employees_hypothesis:
    # check if the number of graduate employees in the hypothesis contradicts the number of level-1 employees in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

