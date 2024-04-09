employees_premise = 72
employees_hypothesis = 62
college_graduates_premise = 30
college_graduates_hypothesis = 30

# the hypothesis talks about the number of employees and college graduates, which is also mentioned in the premise
if employees_hypothesis <= employees_premise:
    # check if the estimate of 'employees_hypothesis' contradicts the number of employees in the premise
    label = "contradiction"
elif college_graduates_hypothesis!= college_graduates_premise:
    # check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
