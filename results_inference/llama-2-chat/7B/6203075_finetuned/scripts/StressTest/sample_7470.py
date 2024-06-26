level_1_employees_premise = 72
level_1_employees_hypothesis = 52
college_graduates_premise = 30
college_graduates_hypothesis = 30

# the hypothesis refers to the number of level-1 employees and college graduates in Listco
if level_1_employees_premise < level_1_employees_hypothesis:
    # check if the number of level-1 employees in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif college_graduates_hypothesis!= college_graduates_premise:
    # check if the number of college graduates in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
