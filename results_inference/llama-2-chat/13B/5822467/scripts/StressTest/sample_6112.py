employees_premise = 60
level1_employees_premise = 30
college_graduates_premise = 30

# define variables for the hypothesis
employees_hypothesis = 80
level1_employees_hypothesis = 30
college_graduates_hypothesis = 30

# check if the number of level 1 employees in the hypothesis contradicts the premise
if level1_employees_hypothesis!= level1_employees_premise:
    label = "contradiction"
elif college_graduates_hypothesis!= college_graduates_premise:
    label = "contradiction"
else:
    # check if the number of employees in the hypothesis is greater than the number of employees in the premise
    if employees_hypothesis > employees_premise:
        label = "entailment"
    else:
        # the hypothesis value is less than or equal to the premise value, so we cannot infer entailment or contradiction
        label = "neutral"

print(label)
