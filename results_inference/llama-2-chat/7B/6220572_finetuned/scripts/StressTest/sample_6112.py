employees_premise = 60
employees_hypothesis = 80
graduates_premise = 30
graduates_hypothesis = 30

# the hypothesis refers to the number of level-1 employees and graduates mentioned in the premise
if employees_hypothesis <= employees_premise:
    # check if the estimate of 'employees_hypothesis' contradicts the number of employees in the premise
    label = "contradiction"
elif graduates_hypothesis!= graduates_premise:
    # check if the number of graduates in the hypothesis contradicts the number of graduates reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
