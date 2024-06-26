employees_premise = 218
employees_hypothesis = 118

# the hypothesis refers to the number of employees at Veridux Corporation mentioned in the premise
if employees_hypothesis!= employees_premise:
    # check if the number of employees in the hypothesis contradicts the number of employees reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
