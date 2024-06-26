employees_veridux_premise = 210
employees_veridux_hypothesis = 510

if employees_veridux_hypothesis >= employees_veridux_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
