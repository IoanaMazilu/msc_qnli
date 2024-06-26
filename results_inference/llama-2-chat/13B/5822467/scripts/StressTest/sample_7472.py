employees_premise = 72
level_1_employees_premise = 30
college_graduates_premise = 30

# define variables for the hypothesis
employees_hypothesis = 62
level_1_employees_hypothesis = 30
college_graduates_hypothesis = 30

# compare the number of level-1 employees in the premise and hypothesis
if level_1_employees_premise!= level_1_employees_hypothesis:
    # check if the number of level-1 employees in the hypothesis contradicts the premise
    label = "contradiction"
elif college_graduates_premise!= college_graduates_hypothesis:
    # check if the number of college graduates in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
