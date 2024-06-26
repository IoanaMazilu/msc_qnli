level1_employees_premise = 72
level1_employees_hypothesis = 62
graduates_premise = 20
graduates_hypothesis = 20

# the hypothesis refers to the number of level-1 employees and college graduates at Listco, as mentioned in the premise
if level1_employees_premise <= level1_employees_hypothesis:
    # check if the estimate of 'level1_employees_hypothesis' contradicts the number of level-1 employees in the premise
    label = "contradiction"
elif graduates_premise != graduates_hypothesis:
    # check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
