employees_premise = 510
employees_hypothesis = 210

# the hypothesis refers to the number of employees at Veridux Corporation mentioned in the premise
if employees_hypothesis >= employees_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
