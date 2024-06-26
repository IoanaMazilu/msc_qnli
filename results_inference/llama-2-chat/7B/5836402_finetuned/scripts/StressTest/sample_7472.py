level1_employees_premise = 72
graduates_premise = 30
level1_employees_hypothesis = 62
graduates_hypothesis = 30

# the hypothesis talks about the number of level-1 employees and graduates, referenced also in the premise
if level1_employees_hypothesis!= level1_employees_premise:
    # check if the number of level-1 employees in the hypothesis contradicts the number of level-1 employees in the premise
    label = "contradiction"
elif graduates_hypothesis!= graduates_premise:
    # check if the number of graduates in the hypothesis contradicts the number of graduates reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
