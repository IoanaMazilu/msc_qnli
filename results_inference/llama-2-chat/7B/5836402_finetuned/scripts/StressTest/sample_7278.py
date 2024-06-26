employees_premise = 210
employees_hypothesis = 510

# the hypothesis talks about the number of employees at Veridux Corporation, referenced also in the premise
if employees_hypothesis >= employees_premise:
    # check if the hypothesis value contradicts the number of employees in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the number of employees in the premise, we can infer entailment
    label = "entailment"

print(label)
