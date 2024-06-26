level1_employees_premise = 60
level1_employees_hypothesis = 80
college_graduates_premise = 30
college_graduates_hypothesis = 30

# the hypothesis talks about the number of level-1 employees and college graduates at Amtek, referenced also in the premise
if level1_employees_hypothesis <= level1_employees_premise:
    # check if the hypothesis value contradicts the estimate of more than 'level1_employees_premise'
    label = "contradiction"
elif college_graduates_hypothesis!= college_graduates_premise:
    # check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of level-1 employees
    # any number of level-1 employees greater than 'level1_employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
