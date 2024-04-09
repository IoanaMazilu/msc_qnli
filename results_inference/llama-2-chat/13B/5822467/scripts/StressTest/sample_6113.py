employees_premise = 80
level_1_employees_premise = 30
college_graduates_premise = 30

# define variables for the hypothesis
employees_hypothesis = 10
level_1_employees_hypothesis = 30
college_graduates_hypothesis = 30

# compare the number of employees in the premise and hypothesis
if employees_premise > employees_hypothesis:
    # the hypothesis does not contradict the premise, but the number of employees in the premise is greater
    label = "neutral"
elif employees_hypothesis > level_1_employees_premise:
    # the hypothesis refers to the number of level 1 employees, which contradicts the premise
    label = "contradiction"
elif college_graduates_hypothesis!= college_graduates_premise:
    # the number of college graduates in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
