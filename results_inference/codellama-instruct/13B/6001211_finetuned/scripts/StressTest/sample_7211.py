employees_premise = 250
employees_hypothesis = 850

# the hypothesis refers to the number of employees at Veridux Corporation mentioned in the premise
if employees_hypothesis!= employees_premise:
    # check if the number of employees in the hypothesis contradicts the number of employees reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
