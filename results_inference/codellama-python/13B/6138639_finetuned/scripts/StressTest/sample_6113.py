level1_employees_premise = 80
level1_employees_hypothesis = 10
college_graduates_premise = 30
college_graduates_hypothesis = 30

# the hypothesis talks about the number of level-1 employees and college graduates at Amtek, referenced also in the premise
if level1_employees_hypothesis > level1_employees_premise:
    # check if the hypothesis value contradicts the number of level-1 employees in the premise
    label = "contradiction"
elif college_graduates_hypothesis!= college_graduates_premise:
    # check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
