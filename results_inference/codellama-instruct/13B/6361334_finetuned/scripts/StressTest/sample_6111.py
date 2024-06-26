employees_premise = 80
college_grads_premise = 30

employees_hypothesis = 60
college_grads_hypothesis = 30

# the hypothesis refers to the number of level-1 employees and college graduates mentioned in the premise
if employees_hypothesis <= employees_premise:
    # check if the estimate of 'employees_hypothesis' contradicts the number of employees in the premise
    label = "contradiction"
elif college_grads_hypothesis!= college_grads_premise:
    # check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
