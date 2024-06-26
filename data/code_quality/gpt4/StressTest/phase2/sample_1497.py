level1_employees_premise = 60
level1_employees_hypothesis = 30
graduates_premise = 30
graduates_hypothesis = 30

# the hypothesis refers to the number of level-1 employees and graduates mentioned in the premise
if level1_employees_premise <= level1_employees_hypothesis:
    # check if the estimate of 'level1_employees_hypothesis' contradicts the number of level-1 employees in the premise
    label = "contradiction"
elif graduates_hypothesis != graduates_premise:
    # check if the number of graduates in the hypothesis contradicts the number of graduates reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
