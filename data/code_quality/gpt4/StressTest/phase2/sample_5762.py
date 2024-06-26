employees_premise = 250
employees_hypothesis = 750

# the hypothesis talks about the number of employees at Veridux Corporation, which is also mentioned in the premise
if employees_hypothesis != employees_premise:
    # check if the number of employees in the hypothesis contradicts the number of employees reported in the premise
    label = "contradiction"
else:
    # since the premise gives a specific number of employees, any number that matches this is considered an entailment
    label = "entailment"

print(label)
