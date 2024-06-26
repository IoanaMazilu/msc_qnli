employees_premise = 72
level_1_employees_premise = 30
college_graduates_premise = 30

hypothesis_employees = 52
hypothesis_level_1_employees = 30
hypothesis_college_graduates = 30

# the hypothesis refers to the number of level-1 employees and college graduates mentioned in the premise
if hypothesis_employees > employees_premise:
    # check if the estimate of 'employees_premise' contradicts the number of employees reported in the hypothesis
    label = "contradiction"
elif hypothesis_level_1_employees!= level_1_employees_premise:
    # check if the number of level-1 employees in the hypothesis contradicts the number of level-1 employees reported in the premise
    label = "contradiction"
elif hypothesis_college_graduates!= college_graduates_premise:
    # check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
