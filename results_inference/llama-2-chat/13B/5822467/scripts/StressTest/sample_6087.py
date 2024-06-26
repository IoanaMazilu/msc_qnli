matt_work_premise = 12
peter_work_premise = 10
matt_work_hypothesis = 52
peter_work_hypothesis = 10

# the hypothesis refers to the number of days Matt and Peter work together
if matt_work_hypothesis < matt_work_premise:
    # check if the hypothesis value contradicts the number of days Matt worked in the premise
    label = "contradiction"
elif peter_work_hypothesis!= peter_work_premise:
    # check if the number of days Peter worked in the hypothesis contradicts the number of days Peter worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
